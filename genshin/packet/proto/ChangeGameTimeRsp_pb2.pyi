from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeGameTimeRsp(_message.Message):
    __slots__ = ("cur_game_time", "extra_days", "retcode")
    CUR_GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DAYS_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    cur_game_time: int
    extra_days: int
    retcode: int
    def __init__(self, cur_game_time: _Optional[int] = ..., extra_days: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
