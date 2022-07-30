from __future__ import annotations

import enum
import datetime
import struct
from typing import Iterator, List

from genshin.packet import opcodes


class Direction(enum.IntEnum):
    SENT = 0
    RECEIVED = 1


class Packet:
    def __init__(
        self, timestamp: datetime.datetime, direction: Direction, content: bytes
    ) -> None:
        self.timestamp = timestamp
        self.direction = direction
        self.content = content

        # Content
        # 0x4567  opcode  hdr_len data_len                                      0x89ab
        # xx xx | xx xx | xx xx | xx xx xx xx | ... header ... | ... data ... | xx xx


class DecryptedPacket:
    def __init__(
        self, timestamp: datetime.datetime, direction: Direction, content: bytes
    ) -> None:
        self.timestamp = timestamp
        self.direction = direction
        self.content = content

        assert content[:2] == b"\x45\x67"
        assert content[-2:] == b"\x89\xab"

        # Content
        # 0x4567  opcode  hdr_len data_len                                      0x89ab
        # xx xx | xx xx | xx xx | xx xx xx xx | ... header ... | ... data ... | xx xx

    @property
    def opcode(self) -> opcodes.Opcode:
        (op,) = struct.unpack(">H", self.content[2:4])
        return opcodes.Opcode(op)

    @property
    def is_compound_packet(self) -> bool:
        return self.opcode in {opcodes.Opcode.UnionCmdNotify}

    @property
    def hdr_len(self) -> bytes:
        (hlen,) = struct.unpack(">H", self.content[4:6])
        return hlen

    @property
    def data_len(self) -> bytes:
        (dlen,) = struct.unpack(">L", self.content[6:10])
        return dlen

    @property
    def data(self) -> bytes:
        hlen = self.hdr_len
        dlen = self.data_len
        assert len(self.content) == 2 + 2 + 2 + 4 + hlen + dlen + 2
        return self.content[2 + 2 + 2 + 4 + hlen : 2 + 2 + 2 + 4 + hlen + dlen]

    def get_sub_packets(self) -> Iterator[DecryptedPacket]:
        assert self.is_compound_packet

        if self.opcode == opcodes.Opcode.UnionCmdNotify:
            from genshin.packet.proto.UnionCmdNotify_pb2 import UnionCmdNotify

            pb = UnionCmdNotify()
            pb.ParseFromString(self.data)

            for cmd in pb.cmd_list:
                yield DecryptedSubPacket(
                    timestamp=self.timestamp,
                    direction=self.direction,
                    opcode=opcodes.Opcode(cmd.message_id),
                    data=cmd.body,
                )
        else:
            assert False


class DecryptedSubPacket:
    def __init__(
        self,
        timestamp: datetime.datetime,
        direction: Direction,
        opcode: opcodes.Opcode,
        data: bytes,
    ) -> None:
        self.timestamp = timestamp
        self.direction = direction
        self.opcode = opcode
        self.data = data
