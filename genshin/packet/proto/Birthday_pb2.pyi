from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Birthday(_message.Message):
    __slots__ = ("month", "day")
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    month: int
    day: int
    def __init__(self, month: _Optional[int] = ..., day: _Optional[int] = ...) -> None: ...
