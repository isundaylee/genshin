from genshin.packet.proto import DJFNBCGCGCP_pb2 as _DJFNBCGCGCP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ENCKBCPPNHG(_message.Message):
    __slots__ = ("NNGFNBCAAPI", "GLKNGDDNOCN", "BDCBLNLCAGE", "MPNJAOCKMAH", "NMAAPLDBBNI")
    NNGFNBCAAPI_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    BDCBLNLCAGE_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    NMAAPLDBBNI_FIELD_NUMBER: _ClassVar[int]
    NNGFNBCAAPI: _containers.RepeatedCompositeFieldContainer[_DJFNBCGCGCP_pb2.DJFNBCGCGCP]
    GLKNGDDNOCN: bool
    BDCBLNLCAGE: bool
    MPNJAOCKMAH: int
    NMAAPLDBBNI: int
    def __init__(self, NNGFNBCAAPI: _Optional[_Iterable[_Union[_DJFNBCGCGCP_pb2.DJFNBCGCGCP, _Mapping]]] = ..., GLKNGDDNOCN: bool = ..., BDCBLNLCAGE: bool = ..., MPNJAOCKMAH: _Optional[int] = ..., NMAAPLDBBNI: _Optional[int] = ...) -> None: ...
