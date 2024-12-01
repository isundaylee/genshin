from genshin.packet.proto import DJFNBCGCGCP_pb2 as _DJFNBCGCGCP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NFEKGKHMLBP(_message.Message):
    __slots__ = ("avatar_list", "BODIEJCLGMB", "MPNJAOCKMAH")
    AVATAR_LIST_FIELD_NUMBER: _ClassVar[int]
    BODIEJCLGMB_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    avatar_list: _containers.RepeatedCompositeFieldContainer[_DJFNBCGCGCP_pb2.DJFNBCGCGCP]
    BODIEJCLGMB: int
    MPNJAOCKMAH: int
    def __init__(self, avatar_list: _Optional[_Iterable[_Union[_DJFNBCGCGCP_pb2.DJFNBCGCGCP, _Mapping]]] = ..., BODIEJCLGMB: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
