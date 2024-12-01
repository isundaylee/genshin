from genshin.packet.proto import CGOIHCDFFEJ_pb2 as _CGOIHCDFFEJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class INOJFJKPAFF(_message.Message):
    __slots__ = ("PMJGJNILMBP", "MPNJAOCKMAH", "HGGEHLMHKMP")
    PMJGJNILMBP_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    HGGEHLMHKMP_FIELD_NUMBER: _ClassVar[int]
    PMJGJNILMBP: _containers.RepeatedCompositeFieldContainer[_CGOIHCDFFEJ_pb2.CGOIHCDFFEJ]
    MPNJAOCKMAH: int
    HGGEHLMHKMP: int
    def __init__(self, PMJGJNILMBP: _Optional[_Iterable[_Union[_CGOIHCDFFEJ_pb2.CGOIHCDFFEJ, _Mapping]]] = ..., MPNJAOCKMAH: _Optional[int] = ..., HGGEHLMHKMP: _Optional[int] = ...) -> None: ...
