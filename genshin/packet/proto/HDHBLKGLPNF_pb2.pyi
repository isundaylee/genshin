from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HDHBLKGLPNF(_message.Message):
    __slots__ = ("GLKNGDDNOCN", "BDCBLNLCAGE", "MPNJAOCKMAH", "MAFDJFNEPHK")
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    BDCBLNLCAGE_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    MAFDJFNEPHK_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN: bool
    BDCBLNLCAGE: bool
    MPNJAOCKMAH: int
    MAFDJFNEPHK: int
    def __init__(self, GLKNGDDNOCN: bool = ..., BDCBLNLCAGE: bool = ..., MPNJAOCKMAH: _Optional[int] = ..., MAFDJFNEPHK: _Optional[int] = ...) -> None: ...
