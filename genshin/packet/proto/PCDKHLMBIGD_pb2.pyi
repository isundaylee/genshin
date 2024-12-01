from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PCDKHLMBIGD(_message.Message):
    __slots__ = ("DDBDIFLNHDG", "MPNJAOCKMAH")
    DDBDIFLNHDG_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    DDBDIFLNHDG: _containers.RepeatedScalarFieldContainer[int]
    MPNJAOCKMAH: int
    def __init__(self, DDBDIFLNHDG: _Optional[_Iterable[int]] = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
