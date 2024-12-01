from genshin.packet.proto import AKKLOINFCPM_pb2 as _AKKLOINFCPM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CLMNDAFKLEL(_message.Message):
    __slots__ = ("LCFAEHIBKFB", "GLKNGDDNOCN", "BDCBLNLCAGE", "MPNJAOCKMAH", "ODCMKOFFKKL")
    LCFAEHIBKFB_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    BDCBLNLCAGE_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    ODCMKOFFKKL_FIELD_NUMBER: _ClassVar[int]
    LCFAEHIBKFB: _containers.RepeatedCompositeFieldContainer[_AKKLOINFCPM_pb2.AKKLOINFCPM]
    GLKNGDDNOCN: bool
    BDCBLNLCAGE: bool
    MPNJAOCKMAH: int
    ODCMKOFFKKL: int
    def __init__(self, LCFAEHIBKFB: _Optional[_Iterable[_Union[_AKKLOINFCPM_pb2.AKKLOINFCPM, _Mapping]]] = ..., GLKNGDDNOCN: bool = ..., BDCBLNLCAGE: bool = ..., MPNJAOCKMAH: _Optional[int] = ..., ODCMKOFFKKL: _Optional[int] = ...) -> None: ...
