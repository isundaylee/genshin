from genshin.packet.proto import CGOIHCDFFEJ_pb2 as _CGOIHCDFFEJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BMAKGNMONKA(_message.Message):
    __slots__ = ("PMJGJNILMBP", "MKCGMMGANLK", "MPNJAOCKMAH", "GLKNGDDNOCN")
    PMJGJNILMBP_FIELD_NUMBER: _ClassVar[int]
    MKCGMMGANLK_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    PMJGJNILMBP: _containers.RepeatedCompositeFieldContainer[_CGOIHCDFFEJ_pb2.CGOIHCDFFEJ]
    MKCGMMGANLK: int
    MPNJAOCKMAH: int
    GLKNGDDNOCN: bool
    def __init__(self, PMJGJNILMBP: _Optional[_Iterable[_Union[_CGOIHCDFFEJ_pb2.CGOIHCDFFEJ, _Mapping]]] = ..., MKCGMMGANLK: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ..., GLKNGDDNOCN: bool = ...) -> None: ...
