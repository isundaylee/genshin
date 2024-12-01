from genshin.packet.proto import DJFNBCGCGCP_pb2 as _DJFNBCGCGCP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PDMEMBBFLGB(_message.Message):
    __slots__ = ("HKECPNIKBIF", "BDCBLNLCAGE", "GLKNGDDNOCN", "MPNJAOCKMAH", "MKCGMMGANLK")
    HKECPNIKBIF_FIELD_NUMBER: _ClassVar[int]
    BDCBLNLCAGE_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    MKCGMMGANLK_FIELD_NUMBER: _ClassVar[int]
    HKECPNIKBIF: _containers.RepeatedCompositeFieldContainer[_DJFNBCGCGCP_pb2.DJFNBCGCGCP]
    BDCBLNLCAGE: bool
    GLKNGDDNOCN: bool
    MPNJAOCKMAH: int
    MKCGMMGANLK: int
    def __init__(self, HKECPNIKBIF: _Optional[_Iterable[_Union[_DJFNBCGCGCP_pb2.DJFNBCGCGCP, _Mapping]]] = ..., BDCBLNLCAGE: bool = ..., GLKNGDDNOCN: bool = ..., MPNJAOCKMAH: _Optional[int] = ..., MKCGMMGANLK: _Optional[int] = ...) -> None: ...
