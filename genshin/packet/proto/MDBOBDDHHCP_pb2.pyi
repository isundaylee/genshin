from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MDBOBDDHHCP(_message.Message):
    __slots__ = ("LPAGGIOGCJK", "DCBDHNJFBDA", "IOELHOCJEHO", "type")
    LPAGGIOGCJK_FIELD_NUMBER: _ClassVar[int]
    DCBDHNJFBDA_FIELD_NUMBER: _ClassVar[int]
    IOELHOCJEHO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LPAGGIOGCJK: _containers.RepeatedScalarFieldContainer[float]
    DCBDHNJFBDA: _containers.RepeatedScalarFieldContainer[int]
    IOELHOCJEHO: int
    type: int
    def __init__(self, LPAGGIOGCJK: _Optional[_Iterable[float]] = ..., DCBDHNJFBDA: _Optional[_Iterable[int]] = ..., IOELHOCJEHO: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...
