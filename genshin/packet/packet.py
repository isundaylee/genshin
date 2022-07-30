import enum
import datetime


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
