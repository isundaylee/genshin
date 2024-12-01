from genshin.packet.proto import LCFCOCGNPOM_pb2 as _LCFCOCGNPOM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HJEPDHKIACB(_message.Message):
    __slots__ = ("MIEAFINBNDK", "GLKNGDDNOCN", "BDCBLNLCAGE", "MPNJAOCKMAH")
    MIEAFINBNDK_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    BDCBLNLCAGE_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    MIEAFINBNDK: _containers.RepeatedCompositeFieldContainer[_LCFCOCGNPOM_pb2.LCFCOCGNPOM]
    GLKNGDDNOCN: bool
    BDCBLNLCAGE: bool
    MPNJAOCKMAH: int
    def __init__(self, MIEAFINBNDK: _Optional[_Iterable[_Union[_LCFCOCGNPOM_pb2.LCFCOCGNPOM, _Mapping]]] = ..., GLKNGDDNOCN: bool = ..., BDCBLNLCAGE: bool = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
