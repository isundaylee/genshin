from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SkipPlayerGameTimeReq(_message.Message):
    __slots__ = ("game_time", "is_force_set", "client_game_time")
    GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_FORCE_SET_FIELD_NUMBER: _ClassVar[int]
    CLIENT_GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    game_time: int
    is_force_set: bool
    client_game_time: int
    def __init__(self, game_time: _Optional[int] = ..., is_force_set: bool = ..., client_game_time: _Optional[int] = ...) -> None: ...
