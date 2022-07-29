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
