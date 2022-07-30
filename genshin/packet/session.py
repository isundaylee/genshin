import collections
import datetime
import socket
import struct
import logging
from typing import Deque, Dict, List, Optional, Tuple

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
    def __init__(self, path: str, my_ip: str) -> None:
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
