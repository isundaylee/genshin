import datetime
import socket
import struct
import logging
from typing import List, Optional

import dpkt

from genshin.packet import packet

logger = logging.getLogger(__name__)


class KCPSession:
    CMD_PUSH = 81
    CMD_ACK = 82
    CMD_WASK = 83
    CMD_WINS = 84

    def __init__(self, name: str):
        self.conv: Optional[int] = None
        self.name = name
        self.logger = logging.getLogger(f"kcp-session-{name}")

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

        self.logger.info(
            "%s %4s %6s wnd %d ts %d sn %d una %d length %4d | %s",
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
            " ".join(f"{b:02x}" for b in data[24 : 24 + min(length, 20)]),
        )

        if cmd == KCPSession.CMD_ACK:
            assert length == 0
        elif cmd == KCPSession.CMD_PUSH:
            pass

        return 24 + length


class Session:
    def __init__(self, path: str, my_ip: str) -> None:
        self.packets: List[packet.Packet] = []

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

                if socket.inet_ntoa(ip.src) == my_ip:
                    self.send_kcp.add_data(timestamp, udp.data)
                    # self.packets.append(
                    #     packet.Packet(
                    #         datetime.datetime.fromtimestamp(ts),
                    #         packet.Direction.SENT,
                    #         udp.data,
                    #     )
                    # )
                elif socket.inet_ntoa(ip.dst) == my_ip:
                    self.receive_kcp.add_data(timestamp, udp.data)
                    # self.packets.append(
                    #     packet.Packet(
                    #         datetime.datetime.fromtimestamp(ts),
                    #         packet.Direction.RECEIVED,
                    #         udp.data,
                    #     )
                    # )
