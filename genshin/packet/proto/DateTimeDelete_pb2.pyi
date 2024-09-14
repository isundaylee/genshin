from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DateTimeDelete(_message.Message):
    __slots__ = ("delete_time",)
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    delete_time: int
    def __init__(self, delete_time: _Optional[int] = ...) -> None: ...
