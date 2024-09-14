from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerGameTimeNotify(_message.Message):
    __slots__ = ("game_time", "is_home", "uid")
    GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_HOME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    game_time: int
    is_home: bool
    uid: int
    def __init__(self, game_time: _Optional[int] = ..., is_home: bool = ..., uid: _Optional[int] = ...) -> None: ...
