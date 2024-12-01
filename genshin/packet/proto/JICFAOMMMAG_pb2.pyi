from genshin.packet.proto import LLGCDCDHDPD_pb2 as _LLGCDCDHDPD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JICFAOMMMAG(_message.Message):
    __slots__ = ("DJMCHFPIFLM", "BDALEDOAHFA", "EJNINFFFKJP", "BHGDNCIOJDJ")
    DJMCHFPIFLM_FIELD_NUMBER: _ClassVar[int]
    BDALEDOAHFA_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    BHGDNCIOJDJ_FIELD_NUMBER: _ClassVar[int]
    DJMCHFPIFLM: _containers.RepeatedCompositeFieldContainer[_LLGCDCDHDPD_pb2.LLGCDCDHDPD]
    BDALEDOAHFA: _LLGCDCDHDPD_pb2.LLGCDCDHDPD
    EJNINFFFKJP: int
    BHGDNCIOJDJ: int
    def __init__(self, DJMCHFPIFLM: _Optional[_Iterable[_Union[_LLGCDCDHDPD_pb2.LLGCDCDHDPD, _Mapping]]] = ..., BDALEDOAHFA: _Optional[_Union[_LLGCDCDHDPD_pb2.LLGCDCDHDPD, _Mapping]] = ..., EJNINFFFKJP: _Optional[int] = ..., BHGDNCIOJDJ: _Optional[int] = ...) -> None: ...
