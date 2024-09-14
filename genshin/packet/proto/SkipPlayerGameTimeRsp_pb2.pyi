from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SkipPlayerGameTimeRsp(_message.Message):
    __slots__ = ("client_game_time", "retcode", "game_time")
    CLIENT_GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    client_game_time: int
    retcode: int
    game_time: int
    def __init__(self, client_game_time: _Optional[int] = ..., retcode: _Optional[int] = ..., game_time: _Optional[int] = ...) -> None: ...
