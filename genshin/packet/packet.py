from __future__ import annotations
import abc

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


class BaseDecryptedPacket(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def raw_opcode(self) -> int:
        pass

    @property
    def opcode(self) -> opcodes.Opcode:
        return opcodes.Opcode(self.raw_opcode)

    @property
    def opcode_name_allow_missing(self) -> str:
        try:
            return opcodes.Opcode(self.raw_opcode).name
        except ValueError:
            return str(self.raw_opcode)

    @property
    @abc.abstractmethod
    def data(self) -> bytes:
        pass

    def string_summary(self) -> str:
        if self.raw_opcode == opcodes.Opcode.SceneEntityDisappearNotify.value:
            from genshin.packet.proto.SceneEntityDisappearNotify_pb2 import (
                SceneEntityDisappearNotify,
            )

            pb = SceneEntityDisappearNotify()
            pb.ParseFromString(self.data)
            return f"disappear_type {pb.disappear_type} param {pb.param}"
        elif self.raw_opcode == opcodes.Opcode.SceneEntityAppearNotify.value:
            from genshin.packet.proto.SceneEntityAppearNotify_pb2 import (
                SceneEntityAppearNotify,
            )

            pb = SceneEntityAppearNotify()
            pb.ParseFromString(self.data)
            return f"appear_type {pb.appear_type} param {pb.param}"
        else:
            return ""


class DecryptedPacket(BaseDecryptedPacket):
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
    def raw_opcode(self) -> int:
        (op,) = struct.unpack(">H", self.content[2:4])
        return op

    @property
    def is_compound_packet(self) -> bool:
        return self.raw_opcode in {opcodes.Opcode.UnionCmdNotify.value}

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

        if self.raw_opcode == opcodes.Opcode.UnionCmdNotify.value:
            from genshin.packet.proto.UnionCmdNotify_pb2 import UnionCmdNotify

            pb = UnionCmdNotify()
            pb.ParseFromString(self.data)

            for cmd in pb.cmd_list:
                yield DecryptedSubPacket(
                    timestamp=self.timestamp,
                    direction=self.direction,
                    raw_opcode=cmd.message_id,
                    data=cmd.body,
                )
        else:
            assert False


class DecryptedSubPacket(BaseDecryptedPacket):
    def __init__(
        self,
        timestamp: datetime.datetime,
        direction: Direction,
        raw_opcode: int,
        data: bytes,
    ) -> None:
        self.timestamp = timestamp
        self.direction = direction
        self._raw_opcode = raw_opcode
        self._data = data

    @property
    def raw_opcode(self) -> int:
        return self._raw_opcode

    @property
    def data(self) -> bytes:
        return self._data
