from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RogueDiaryDungeonSettleNotify(_message.Message):
    __slots__ = ("explore_time", "is_finish", "cur_round")
    EXPLORE_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_FINISH_FIELD_NUMBER: _ClassVar[int]
    CUR_ROUND_FIELD_NUMBER: _ClassVar[int]
    explore_time: int
    is_finish: bool
    cur_round: int
    def __init__(self, explore_time: _Optional[int] = ..., is_finish: bool = ..., cur_round: _Optional[int] = ...) -> None: ...
