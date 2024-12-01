from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PMBKMCCIMNE(_message.Message):
    __slots__ = ("GPDEPMCLKMM", "MBBKAENBCKD", "MPNJAOCKMAH")
    GPDEPMCLKMM_FIELD_NUMBER: _ClassVar[int]
    MBBKAENBCKD_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    GPDEPMCLKMM: _containers.RepeatedScalarFieldContainer[int]
    MBBKAENBCKD: int
    MPNJAOCKMAH: int
    def __init__(self, GPDEPMCLKMM: _Optional[_Iterable[int]] = ..., MBBKAENBCKD: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
