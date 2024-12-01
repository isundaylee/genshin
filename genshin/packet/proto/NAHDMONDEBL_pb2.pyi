from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NAHDMONDEBL(_message.Message):
    __slots__ = ("MNCHCGGMLPA", "IBIONJBKDDB")
    MNCHCGGMLPA_FIELD_NUMBER: _ClassVar[int]
    IBIONJBKDDB_FIELD_NUMBER: _ClassVar[int]
    MNCHCGGMLPA: _containers.RepeatedScalarFieldContainer[int]
    IBIONJBKDDB: int
    def __init__(self, MNCHCGGMLPA: _Optional[_Iterable[int]] = ..., IBIONJBKDDB: _Optional[int] = ...) -> None: ...
