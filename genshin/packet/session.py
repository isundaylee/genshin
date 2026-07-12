from __future__ import annotations

import collections
import datetime
import itertools
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

    @staticmethod
    def _decode_ip_packet(pkt: bytes, datalink: int) -> Optional[dpkt.ip.IP]:
        if datalink == dpkt.pcap.DLT_EN10MB:
            link_packet = dpkt.ethernet.Ethernet(pkt)
            if link_packet.type != dpkt.ethernet.ETH_TYPE_IP:
                return None
        elif datalink == dpkt.pcap.DLT_LINUX_SLL:
            link_packet = dpkt.sll.SLL(pkt)
            if link_packet.ethtype != dpkt.ethernet.ETH_TYPE_IP:
                return None
        elif datalink == dpkt.pcap.DLT_LINUX_SLL2:
            link_packet = dpkt.sll2.SLL2(pkt)
            if link_packet.ethtype != dpkt.ethernet.ETH_TYPE_IP:
                return None
        else:
            raise ValueError(f"Unsupported pcap link type: {datalink}")

        packet_ip = link_packet.data
        assert isinstance(packet_ip, dpkt.ip.IP)
        return packet_ip

    def __init__(self, path: str, *, copy_key_from: Optional[Session] = None) -> None:
        self.packets: List[packet.Packet] = []
        self.udp_logger = logging.getLogger("udp-session")
        self.kcp_out_logger = logging.getLogger("kcp-out")

        self.send_kcp = KCPSession("sent")
        self.receive_kcp = KCPSession("received")

        with open(path, "rb") as f:
            reader = dpkt.pcap.Reader(f)
            datalink = reader.datalink()
            for ts, pkt in reader:
                packet_ip = self._decode_ip_packet(pkt, datalink)
                if packet_ip is None:
                    continue

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

        # Recover the first 16 bytes of the XOR key from known plaintext, then
        # use find_seed to recover the MT64 seed and generate the full key.
        #
        # This approach is version-independent: it does not rely on any specific
        # opcode values or protobuf field numbers. Known-plaintext sources:
        #
        #   1. Every dispatch packet starts with magic \x45\x67  -> key[0:2]
        #   2. Every dispatch packet ends with magic \x89\xab    -> key[L-2:L]
        #   3. Empty packets (len 12, no header/data)             -> key[4:10]
        #   4. RTT packets (periodic, varying ping)               -> fills gaps
        #
        # key[2:4] (the opcode field) is always unknown and brute-forced via
        # find_seed, which validates candidate keys against MT64 structure.

        # Step 1: Identify the dispatch head (encrypted \x45\x67), which is the
        # most common 2-byte prefix among all reassembled KCP packets.
        head_counts: collections.Counter = collections.Counter(
            p.content[:2] for p in self.packets
        )
        raw_dispatch_head = head_counts.most_common(1)[0][0]
        dispatch_packets = [
            p for p in self.packets if p.content[:2] == raw_dispatch_head
        ]

        logger.debug(
            "Dispatch head %s: %d dispatch packets out of %d total",
            format_bytes(raw_dispatch_head),
            len(dispatch_packets),
            len(self.packets),
        )

        # Step 2: Collect known key byte positions from known plaintext.
        known: Dict[int, int] = {}

        # Every dispatch packet starts with \x45\x67
        for i, b in enumerate(_xor_bytes(b"\x45\x67", raw_dispatch_head)):
            known[i] = b

        # Every dispatch packet ends with \x89\xab
        for p in dispatch_packets:
            L = len(p.content)
            known[L - 2] = p.content[L - 2] ^ 0x89
            known[L - 1] = p.content[L - 1] ^ 0xAB

        # Empty packets (total len 12 = 2+2+2+4+0+0+2): the middle bytes
        # plaintext[4:10] are all \x00 (hdr_len=0, data_len=0).
        for p in dispatch_packets:
            if len(p.content) == 12:
                for i in range(4, 10):
                    known[i] = p.content[i]

        # Step 3: Use RTT (ping) packets to fill remaining gaps in key[10:16].
        self._derive_rtt_key_bytes(dispatch_packets, known)

        # Step 4: Brute-force unknown positions in key[0:16] via find_seed.
        unknown = sorted(set(range(16)) - set(known))
        logger.info(
            "Key inference: %d/%d bytes known, %d unknown positions %s",
            16 - len(unknown),
            16,
            len(unknown),
            unknown,
        )

        if len(unknown) > 3:
            raise RuntimeError(
                f"Too many unknown key byte positions {unknown}; "
                f"need more known-plaintext sources"
            )

        key_template = bytearray(16)
        for i in range(16):
            if i in known:
                key_template[i] = known[i]

        seed: Optional[int] = None
        for combo in itertools.product(range(256), repeat=len(unknown)):
            key_arr = bytearray(key_template)
            for pos, val in zip(unknown, combo):
                key_arr[pos] = val
            key0, key1 = struct.unpack(">QQ", key_arr)
            if (candidate := genshin_xor_key.find_seed(key0, key1)) is not None:
                seed = candidate
                logger.info("Found MT64 seed: %016x", seed)
                break

        if seed is None:
            raise RuntimeError("Failed to find MT64 seed")

        # Generate the full 4096-byte XOR key from the seed.
        mt64 = genshin_xor_key.MT64(seed)
        mt64.generate()
        xor_key = b"".join(
            struct.pack(">Q", mt64.generate()) for _ in range(4096 // 8)
        )
        logger.debug("Generated XOR key: %s", format_bytes(xor_key))

        self.raw_dispatch_head = raw_dispatch_head
        self.xor_key = xor_key
        return raw_dispatch_head, xor_key

    def _derive_rtt_key_bytes(
        self,
        dispatch_packets: List[packet.Packet],
        known: Dict[int, int],
    ) -> None:
        """Derive key bytes from periodic RTT (ping) packets.

        WorldPlayerRTTNotify is sent periodically by the server and contains
        the player's current RTT. The RTT varies slightly (~150ms), creating
        exactly one varying byte in the encrypted packet data. For RTT > 127
        the varint is 2 bytes; the second (continuation) byte is constant 0x01,
        which gives us a known-plaintext byte we can use to recover the key.
        """
        # Find candidate RTT packets: the signature of WorldPlayerRTTNotify is
        # a stream of periodic received packets of the same small size with
        # exactly ONE varying byte (the ping value). Scan all candidate sizes
        # rather than just the most common.
        received_sizes: collections.Counter = collections.Counter(
            len(p.content) for p in dispatch_packets
            if p.direction == packet.Direction.RECEIVED
        )

        rtt_packets: Optional[List[packet.Packet]] = None
        varying_pos: Optional[int] = None
        for sz, cnt in received_sizes.most_common():
            if cnt < 5 or not (16 <= sz <= 40):
                continue

            candidates = [
                p for p in dispatch_packets
                if len(p.content) == sz
                and p.direction == packet.Direction.RECEIVED
            ]

            # Determine data region (10 + hdr_len .. sz - 2)
            if all(i in known for i in (4, 5)):
                hlen = struct.unpack(
                    ">H",
                    bytes([
                        candidates[0].content[4] ^ known[4],
                        candidates[0].content[5] ^ known[5],
                    ]),
                )[0]
                ds = 10 + hlen
            else:
                ds = 10
            de = sz - 2

            vp = [
                i for i in range(ds, de)
                if len(set(p.content[i] for p in candidates)) > 1
            ]
            if len(vp) == 1:
                rtt_packets = candidates
                varying_pos = vp[0]
                data_start = ds
                data_end = de
                break

        if rtt_packets is None or varying_pos is None:
            logger.debug("No RTT packet candidates with exactly 1 varying byte")
            return

        logger.debug(
            "Found %d RTT packets of size %d, varying byte at position %d",
            len(rtt_packets),
            len(rtt_packets[0].content),
            varying_pos,
        )

        # The varying byte is the low byte of the RTT varint. For RTT > 127ms
        # (2-byte varint), the following byte is the continuation byte and is
        # constant 0x01 across all RTT packets.
        next_pos = varying_pos + 1
        if next_pos < data_end and next_pos not in known:
            derived = rtt_packets[0].content[next_pos] ^ 0x01
            known[next_pos] = derived
            logger.debug("RTT analysis derived key[%d] = %02x", next_pos, derived)

    def get_decrypted_packets(self) -> Iterator[packet.DecryptedPacket]:
        if self.copy_key_from is None:
            raw_dispatch_head, xor_key = self._infer_xor_key()
        else:
            # Ensure the source session has inferred its key.
            if not hasattr(self.copy_key_from, "xor_key"):
                self.copy_key_from._infer_xor_key()
            raw_dispatch_head = self.copy_key_from.raw_dispatch_head
            xor_key = self.copy_key_from.xor_key

        for p in self.packets:
            if p.content[:2] != raw_dispatch_head:
                continue

            yield packet.DecryptedPacket(
                timestamp=p.timestamp,
                direction=p.direction,
                content=_xor_bytes_repeat(p.content, xor_key),
            )
