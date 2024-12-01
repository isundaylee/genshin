from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OOIMBBPDCMM(_message.Message):
    __slots__ = ("JPDLCDGLLAC", "MPNJAOCKMAH", "BDCBLNLCAGE", "GLKNGDDNOCN")
    JPDLCDGLLAC_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    BDCBLNLCAGE_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    JPDLCDGLLAC: _containers.RepeatedScalarFieldContainer[int]
    MPNJAOCKMAH: int
    BDCBLNLCAGE: bool
    GLKNGDDNOCN: bool
    def __init__(self, JPDLCDGLLAC: _Optional[_Iterable[int]] = ..., MPNJAOCKMAH: _Optional[int] = ..., BDCBLNLCAGE: bool = ..., GLKNGDDNOCN: bool = ...) -> None: ...
