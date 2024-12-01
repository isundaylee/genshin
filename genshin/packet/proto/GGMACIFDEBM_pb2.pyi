from genshin.packet.proto import IBCBPJIEAAF_pb2 as _IBCBPJIEAAF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GGMACIFDEBM(_message.Message):
    __slots__ = ("HGKBEDPKPNA", "KEPLHHEHOLE", "GLKNGDDNOCN", "MPNJAOCKMAH")
    HGKBEDPKPNA_FIELD_NUMBER: _ClassVar[int]
    KEPLHHEHOLE_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    HGKBEDPKPNA: _containers.RepeatedCompositeFieldContainer[_IBCBPJIEAAF_pb2.IBCBPJIEAAF]
    KEPLHHEHOLE: bool
    GLKNGDDNOCN: bool
    MPNJAOCKMAH: int
    def __init__(self, HGKBEDPKPNA: _Optional[_Iterable[_Union[_IBCBPJIEAAF_pb2.IBCBPJIEAAF, _Mapping]]] = ..., KEPLHHEHOLE: bool = ..., GLKNGDDNOCN: bool = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
