from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassCycle(_message.Message):
    __slots__ = ("begin_time", "cycle_idx", "end_time")
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    CYCLE_IDX_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    begin_time: int
    cycle_idx: int
    end_time: int
    def __init__(self, begin_time: _Optional[int] = ..., cycle_idx: _Optional[int] = ..., end_time: _Optional[int] = ...) -> None: ...
