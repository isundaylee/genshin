import enum
import datetime
import struct

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
