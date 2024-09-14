from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerTimeNotify(_message.Message):
    __slots__ = ("is_paused", "server_time", "player_time")
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_TIME_FIELD_NUMBER: _ClassVar[int]
    is_paused: bool
    server_time: int
    player_time: int
    def __init__(self, is_paused: bool = ..., server_time: _Optional[int] = ..., player_time: _Optional[int] = ...) -> None: ...
