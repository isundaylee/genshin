from __future__ import annotations

import collections
import datetime
import struct
import logging
from typing import ClassVar, Deque, Dict, Iterator, List, Optional, Tuple

import dpkt  # type: ignore

from genshin.packet import opcodes, packet
from genshin.extensions import genshin_xor_key

logger = logging.getLogger(__name__)


def format_bytes(data: bytes, start: int = 20, end: int = 4) -> str:
    def _format_as_hex(d: bytes) -> str:
        return " ".join(f"{b:02x}" for b in d)

    if len(data) <= start:
        return _format_as_hex(data)

    if len(data) <= start + end:
        return _format_as_hex(data[:start]) + "     " + _format_as_hex(data[start:])

    return _format_as_hex(data[:start]) + " ... " + _format_as_hex(data[-end:])


def _xor_bytes(a: bytes, b: bytes) -> bytes:
    assert len(a) == len(b)
    return bytes(x ^ y for x, y in zip(a, b))


def _xor_bytes_repeat(a: bytes, key: bytes) -> bytes:
    if len(a) <= len(key):
        return _xor_bytes(a, key[: len(a)])

    return _xor_bytes(a[: len(key)], key) + _xor_bytes_repeat(a[len(key) :], key)


class KCPSession:
    CMD_PUSH = 0x51
    CMD_ACK = 0x52
    CMD_WASK = 0x53
    CMD_WINS = 0x54

    def __init__(self, name: str):
        self.conv: Optional[int] = None
        self.name = name
        self.logger = logging.getLogger(f"kcp-session-{name}")

        self._last_delivered_sn = -1
        self._pending_packets: Dict[int, Tuple[int, bytes]] = {}
        self._recv_queue: Deque[Tuple[int, bytes]] = collections.deque()

    def add_data(self, timestamp: datetime.datetime, data: bytes) -> None:
        while data:
            # 4 bytes: 2b ee 00 00
            # n bytes: _add_packet
            consumed_length = 4 + self._add_packet(timestamp, data[4:])
            data = data[consumed_length:]

    def _add_packet(self, timestamp: datetime.datetime, data: bytes) -> int:
        assert len(data) >= 28

        conv, cmd, frg, wnd, ts, sn, una, length, hash = struct.unpack(
            "<LccHLLLLL", data[:28]
        )
        cmd = ord(cmd)
        frg = ord(frg)

        if self.conv is None:
            self.conv = conv
        else:
            assert self.conv == conv

        if cmd == KCPSession.CMD_ACK:
            assert length == 0
        elif cmd == KCPSession.CMD_PUSH:
            self._handle_push(sn, frg, data[28 : 28 + length])
        elif cmd == KCPSession.CMD_WASK:
            pass
        elif cmd == KCPSession.CMD_WINS:
            pass
        else:
            assert False, f"Unexpected cmd {cmd}"

        self.logger.debug(
            "%s %4s %8s wnd %5d ts %d sn %5d una %5d length %4d | pending %3d rcvq %3d | %s",
            timestamp.strftime("%Y%m%d-%H:%M:%S.%f"),
            {
                KCPSession.CMD_PUSH: "PUSH",
                KCPSession.CMD_ACK: "ACK",
                KCPSession.CMD_WASK: "WASK",
                KCPSession.CMD_WINS: "WINS",
            }[cmd],
            "" if frg == 0 else f"frg {frg}",
            wnd,
            ts,
            sn,
            una,
            length,
            len(self._pending_packets),
            len(self._recv_queue),
            format_bytes(data[28 : 28 + length]),
        )

        return 28 + length

    def _handle_push(self, sn: int, frg: int, data: bytes) -> None:
        if self._last_delivered_sn == -1:
            self._last_delivered_sn = sn - 1

        if sn <= self._last_delivered_sn:
            self.logger.debug(
                "Received delivered dup with sn %d of size %d bytes", sn, len(data)
            )
            return

        if sn in self._pending_packets:
            assert (frg, data) == self._pending_packets[sn]
            self.logger.warning(
                "Received pending dup with sn %d frg %d of size %d bytes",
                sn,
                frg,
                len(data),
            )
            return

        self._pending_packets[sn] = (frg, data)

        while self._last_delivered_sn + 1 in self._pending_packets:
            self._last_delivered_sn += 1
            self._recv_queue.append(self._pending_packets[self._last_delivered_sn])
            del self._pending_packets[self._last_delivered_sn]

    def receive(self) -> Optional[bytes]:
        for i in range(len(self._recv_queue)):
            frg, _ = self._recv_queue[i]

            if frg != 0:
                continue

            full_data = b""
            for j in range(i + 1):
                frag_frg, frag_data = self._recv_queue.popleft()
                assert frag_frg == i - j
                full_data += frag_data

            return full_data

        return None


class Session:
    _UDP_PORTS: ClassVar[frozenset[int]] = frozenset({22101, 22102})

    def __init__(self, path: str, *, copy_key_from: Optional[Session] = None) -> None:
        self.packets: List[packet.Packet] = []
        self.udp_logger = logging.getLogger("udp-session")
        self.kcp_out_logger = logging.getLogger("kcp-out")

        self.send_kcp = KCPSession("sent")
        self.receive_kcp = KCPSession("received")

        with open(path, "rb") as f:
            for ts, pkt in dpkt.pcap.Reader(f):
                packet_eth = dpkt.ethernet.Ethernet(pkt)
                if packet_eth.type != dpkt.ethernet.ETH_TYPE_IP:
                    continue

                packet_ip = packet_eth.data
                if packet_ip.p != dpkt.ip.IP_PROTO_UDP:
                    continue

                packet_udp = packet_ip.data
                timestamp = datetime.datetime.fromtimestamp(ts)
                # TODO this is not robust
                is_kcp_packet = len(packet_udp.data) > 20

                if packet_udp.dport in self._UDP_PORTS:
                    self.udp_logger.debug("send %s", format_bytes(packet_udp.data))

                    if is_kcp_packet:
                        self.send_kcp.add_data(timestamp, packet_udp.data)

                    while True:
                        kcp_out_packet = self.send_kcp.receive()
                        if kcp_out_packet is None:
                            break

                        self.kcp_out_logger.debug(
                            "send kcp packet len %5d", len(kcp_out_packet)
                        )

                        self.packets.append(
                            packet.Packet(
                                datetime.datetime.fromtimestamp(ts),
                                packet.Direction.SENT,
                                kcp_out_packet,
                            )
                        )
                elif packet_udp.sport in self._UDP_PORTS:
                    self.udp_logger.debug("recv %s", format_bytes(packet_udp.data))

                    if is_kcp_packet:
                        self.receive_kcp.add_data(timestamp, packet_udp.data)

                    while True:
                        kcp_out_packet = self.receive_kcp.receive()
                        if kcp_out_packet is None:
                            break

                        self.kcp_out_logger.debug(
                            "recv kcp packet len %5d", len(kcp_out_packet)
                        )

                        self.packets.append(
                            packet.Packet(
                                datetime.datetime.fromtimestamp(ts),
                                packet.Direction.RECEIVED,
                                kcp_out_packet,
                            )
                        )
                    else:
                        continue

        self.copy_key_from = copy_key_from

    def _infer_xor_key(self) -> tuple[bytes, bytes]:
        assert self.packets

        # raw_ means what we received
        # dec_ means after XOR decryption

        # First, infer the first 16 bytes of the XAR key based on packet format
        # and WorldPlayerRTTNotify format.

        raw_dispatch_head = self.packets[0].content[:2]
        potential_key = b""

        for p in self.packets:
            if p.content[:2] != raw_dispatch_head and (len(potential_key) == 0):
                potential_key += _xor_bytes(
                    b"\x45\x67"
                    + struct.pack(">H", opcodes.Opcode.PlayerLoginReq.value),
                    p.content[:4],
                )
                continue

            if len(potential_key) == 4:
                decrypted_4b = _xor_bytes(p.content[:4], potential_key[:4])
                assert decrypted_4b[:2] == b"\x45\x67"
                logger.debug(
                    "Packet len %d with cmdid %d",
                    len(p.content),
                    struct.unpack(">H", decrypted_4b[2:])[0],
                )

            if len(potential_key) == 4 and (
                p.content[:4]
                == _xor_bytes(
                    b"\x45\x67"
                    + struct.pack(">H", opcodes.Opcode.WorldPlayerRTTNotify.value),
                    potential_key,
                )
            ):
                assert len(p.content) == 22

                # Case 1 - rtt before uid

                # NOTE that byte 13 is (part of) the variable RTT - we will try
                # all 256 values below.
                # potential_key += _xor_bytes(
                #     #                                 ------------------------ WorldPlayerRTTNotify
                #     #                                         ---------------- PlayerRTTInfo
                #     #                                         ------------     rtt
                #     b"\x00\x00" b"\x00\x00\x00\x0a" b"\x12\x08\x10\x00\x01\x58",
                #     p.content[4:16],
                # )
                # unknown_byte_idx = 13

                # Case 2 - uid before rtt
                # NOTE that we enumerate all 256 possibilities for byte 12 (uid
                # field index) below.
                potential_key += _xor_bytes(
                    #                                 ------------------------ WorldPlayerRTTNotify
                    #                                         ---------------- PlayerRTTInfo
                    #                                         ---------------- uid
                    b"\x00\x00" b"\x00\x00\x00\x0a" b"\x22\x08\x00\xb7\xca\xd6",
                    p.content[4:16],
                )
                unknown_byte_idx = 12
                break

        assert len(potential_key) == 16
        logger.debug("XOR key inferred so far: %s", format_bytes(potential_key))

        # Next, find the MT64 rng seed. NOTE that we need to try all 256 values
        # for byte 12/13 of the XOR key.
        for rtt_byte in range(256):
            potential_key_arr = bytearray(potential_key)
            potential_key_arr[unknown_byte_idx] = rtt_byte

            [key0, key1] = struct.unpack(">QQ", potential_key_arr)
            if (seed := genshin_xor_key.find_seed(key0, key1)) is not None:
                logger.info("Found MT64 seed: %016x", seed)
                break
        else:
            raise RuntimeError("Failed to find MT64 seed")

        # Now, generate the full XOR key.
        mt64 = genshin_xor_key.MT64(seed)
        mt64.generate()
        xor_key = b"".join(struct.pack(">Q", mt64.generate()) for _ in range(4096 // 8))
        logger.info("Generated XOR key: %s", format_bytes(xor_key))

        return raw_dispatch_head, xor_key

    def get_decrypted_packets(self) -> Iterator[packet.DecryptedPacket]:
        if self.copy_key_from is None:
            raw_dispatch_head, xor_key = self._infer_xor_key()
        else:
            raw_dispatch_head = self.copy_key_from.raw_dispatch_head
            xor_key = self.copy_key_from.xor_key

        for p in self.packets:
            if p.content[:2] == raw_dispatch_head:
                continue

            yield packet.DecryptedPacket(
                timestamp=p.timestamp,
                direction=p.direction,
                content=_xor_bytes_repeat(p.content, xor_key),
            )
