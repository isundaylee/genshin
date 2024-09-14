from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeGameTimeReq(_message.Message):
    __slots__ = ("is_force_set", "game_time", "extra_days")
    IS_FORCE_SET_FIELD_NUMBER: _ClassVar[int]
    GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DAYS_FIELD_NUMBER: _ClassVar[int]
    is_force_set: bool
    game_time: int
    extra_days: int
    def __init__(self, is_force_set: bool = ..., game_time: _Optional[int] = ..., extra_days: _Optional[int] = ...) -> None: ...
