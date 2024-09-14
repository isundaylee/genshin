from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UgcMusicNote(_message.Message):
    __slots__ = ("start_time", "end_time")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: int
    end_time: int
    def __init__(self, start_time: _Optional[int] = ..., end_time: _Optional[int] = ...) -> None: ...
