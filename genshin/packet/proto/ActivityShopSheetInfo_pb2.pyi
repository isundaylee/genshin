from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityShopSheetInfo(_message.Message):
    __slots__ = ("begin_time", "sheet_id", "end_time")
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    SHEET_ID_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    begin_time: int
    sheet_id: int
    end_time: int
    def __init__(self, begin_time: _Optional[int] = ..., sheet_id: _Optional[int] = ..., end_time: _Optional[int] = ...) -> None: ...
