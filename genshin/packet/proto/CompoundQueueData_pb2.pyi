from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CompoundQueueData(_message.Message):
    __slots__ = ("outputTime", "waitCount", "compound_id", "outputCount")
    OUTPUTTIME_FIELD_NUMBER: _ClassVar[int]
    WAITCOUNT_FIELD_NUMBER: _ClassVar[int]
    COMPOUND_ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUTCOUNT_FIELD_NUMBER: _ClassVar[int]
    outputTime: int
    waitCount: int
    compound_id: int
    outputCount: int
    def __init__(self, outputTime: _Optional[int] = ..., waitCount: _Optional[int] = ..., compound_id: _Optional[int] = ..., outputCount: _Optional[int] = ...) -> None: ...
