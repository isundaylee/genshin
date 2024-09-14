from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityScheduleInfo(_message.Message):
    __slots__ = ("begin_time", "activity_id", "is_open", "end_time", "schedule_id")
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    begin_time: int
    activity_id: int
    is_open: bool
    end_time: int
    schedule_id: int
    def __init__(self, begin_time: _Optional[int] = ..., activity_id: _Optional[int] = ..., is_open: bool = ..., end_time: _Optional[int] = ..., schedule_id: _Optional[int] = ...) -> None: ...
