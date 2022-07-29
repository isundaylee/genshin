import datetime
import socket
from typing import List

import dpkt

from genshin.packet import packet


class Session:
    def __init__(self, path: str, my_ip: str) -> None:
        self.packets: List[packet.Packet] = []

        with open(path, "rb") as f:
            for ts, pkt in dpkt.pcap.Reader(f):
                eth = dpkt.ethernet.Ethernet(pkt)
                assert eth.type == dpkt.ethernet.ETH_TYPE_IP
                ip = eth.data
                assert ip.p == dpkt.ip.IP_PROTO_UDP
                udp = ip.data

                if socket.inet_ntoa(ip.src) == my_ip:
                    self.packets.append(
                        packet.Packet(
                            datetime.datetime.fromtimestamp(ts),
                            packet.Direction.SENT,
                            udp.data,
                        )
                    )
                elif socket.inet_ntoa(ip.dst) == my_ip:
                    self.packets.append(
                        packet.Packet(
                            datetime.datetime.fromtimestamp(ts),
                            packet.Direction.RECEIVED,
                            udp.data,
                        )
                    )
