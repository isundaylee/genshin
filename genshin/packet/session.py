from __future__ import annotations

import collections
import datetime
import os
import socket
import struct
import logging
from typing import Deque, Dict, Iterator, List, Optional, Tuple

import dpkt

from genshin.packet import packet

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
    CMD_PUSH = 81
    CMD_ACK = 82
    CMD_WASK = 83
    CMD_WINS = 84

    def __init__(self, name: str):
        self.conv: Optional[int] = None
        self.name = name
        self.logger = logging.getLogger(f"kcp-session-{name}")

        self._last_delivered_sn = -1
        self._pending_packets: Dict[int, Tuple[int, bytes]] = {}
        self._recv_queue: Deque[Tuple[int, bytes]] = collections.deque()

    def add_data(self, timestamp: datetime.datetime, data: bytes) -> Optional[bytes]:
        while data:
            consumed_length = 4 + self._add_packet(timestamp, data[4:])
            data = data[consumed_length:]

    def _add_packet(self, timestamp: datetime.datetime, data: bytes) -> int:
        assert len(data) >= 24

        conv, cmd, frg, wnd, ts, sn, una, length = struct.unpack("<LccHLLLL", data[:24])
        cmd = ord(cmd)
        frg = ord(frg)

        if self.conv is None:
            self.conv = conv
        else:
            assert self.conv == conv

        if cmd == KCPSession.CMD_ACK:
            assert length == 0
        elif cmd == KCPSession.CMD_PUSH:
            self._handle_push(sn, frg, data[24 : 24 + length])
            pass
        else:
            assert False, f"Unexpected cmd {cmd}"

        self.logger.info(
            "%s %4s %6s wnd %5d ts %d sn %5d una %5d length %4d | pending %3d rcvq %3d | %s",
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
            format_bytes(data[24 : 24 + length]),
        )

        return 24 + length

    def _handle_push(self, sn: int, frg: int, data: bytes) -> None:
        if self._last_delivered_sn == -1:
            self._last_delivered_sn = sn - 1

        if sn <= self._last_delivered_sn:
            self.logger.warning(
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
    def __init__(
        self, path: str, my_ip: str, *, copy_key_from: Optional[Session] = None
    ) -> None:
        self.packets: List[packet.Packet] = []
        self.udp_logger = logging.getLogger("udp-session")
        self.kcp_out_logger = logging.getLogger("kcp-out")

        self.send_kcp = KCPSession("sent")
        self.receive_kcp = KCPSession("received")

        with open(path, "rb") as f:
            for ts, pkt in dpkt.pcap.Reader(f):
                eth = dpkt.ethernet.Ethernet(pkt)
                assert eth.type == dpkt.ethernet.ETH_TYPE_IP
                ip = eth.data
                assert ip.p == dpkt.ip.IP_PROTO_UDP
                udp = ip.data

                timestamp = datetime.datetime.fromtimestamp(ts)

                # TODO this is not robust
                is_kcp_packet = len(udp.data) > 20

                if socket.inet_ntoa(ip.src) == my_ip:
                    self.udp_logger.info("send %s", format_bytes(udp.data))

                    if is_kcp_packet:
                        self.send_kcp.add_data(timestamp, udp.data)

                    while True:
                        kcp_out_packet = self.send_kcp.receive()
                        if kcp_out_packet is None:
                            break

                        self.kcp_out_logger.info(
                            "send kcp packet len %5d", len(kcp_out_packet)
                        )

                        self.packets.append(
                            packet.Packet(
                                datetime.datetime.fromtimestamp(ts),
                                packet.Direction.SENT,
                                kcp_out_packet,
                            )
                        )
                elif socket.inet_ntoa(ip.dst) == my_ip:
                    self.udp_logger.info("recv %s", format_bytes(udp.data))

                    if is_kcp_packet:
                        self.receive_kcp.add_data(timestamp, udp.data)

                    while True:
                        kcp_out_packet = self.receive_kcp.receive()
                        if kcp_out_packet is None:
                            break

                        self.kcp_out_logger.info(
                            "recv kcp packet len %5d", len(kcp_out_packet)
                        )

                        self.packets.append(
                            packet.Packet(
                                datetime.datetime.fromtimestamp(ts),
                                packet.Direction.RECEIVED,
                                kcp_out_packet,
                            )
                        )

        if copy_key_from is None:
            self.raw_dispatch_head, self.xor_key = self._infer_xor_key()
        else:
            self.raw_dispatch_head = copy_key_from.raw_dispatch_head
            self.xor_key = copy_key_from.xor_key

    def _infer_xor_key(self) -> None:
        assert self.packets

        # raw_ means what we received
        # dec_ means after XOR decryption

        raw_dispatch_head = self.packets[0].content[:2]
        potential_key = b""

        for p in self.packets:
            if p.content[:2] != raw_dispatch_head and (len(potential_key) == 0):
                # This is the PlayerLoginReq
                potential_key += _xor_bytes(b"\x45\x67\x00\x70", p.content[:4])
                continue

            if len(potential_key) == 4 and (
                p.content[:4] == _xor_bytes(b"\x45\x67\x00\x16", potential_key)
            ):
                # This is the WorldPlayerRTTNotify
                potential_key += _xor_bytes(b"\x00\x00", p.content[4:6])
                break

        assert len(potential_key) == 6

        for p in self.packets:
            if _xor_bytes(p.content[:4], potential_key[:4]) != b"\x45\x67\x04\xaf":
                continue

            (hlen,) = struct.unpack(
                ">H", _xor_bytes(p.content[4:6], potential_key[4:6])
            )
            content_start_offset = 2 + 2 + 2 + 4 + hlen
            raw_data_content = p.content[content_start_offset:-2]

            with open(
                os.path.join(
                    os.path.dirname(__file__),
                    "..",
                    "..",
                    "resources",
                    "initial_WindSeedClientNotify_content.bin",
                ),
                "rb",
            ) as f:
                # The key I received for 3.1 starts 8 bytes later than the
                # previous one. Pad it here.
                plaintext_content = (b" " * 8) + f.read()[:-2]

            logger.info("raw_data_content has length %d", len(raw_data_content))

            full_xor_key = _xor_bytes(raw_data_content[:8192], plaintext_content[:8192])
            xor_key = full_xor_key[
                4096 - content_start_offset : 4096 + 4096 - content_start_offset
            ]
            assert xor_key[: len(potential_key)] == potential_key
            assert len(xor_key) == 4096

            return raw_dispatch_head, xor_key

        assert False

    def get_decrypted_packets(self) -> Iterator[packet.DecryptedPacket]:
        for p in self.packets:
            if p.content[:2] == self.raw_dispatch_head:
                continue

            yield packet.DecryptedPacket(
                timestamp=p.timestamp,
                direction=p.direction,
                content=_xor_bytes_repeat(p.content, self.xor_key),
            )
