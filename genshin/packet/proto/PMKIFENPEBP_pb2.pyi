from genshin.packet.proto import NGOFPEOLOPF_pb2 as _NGOFPEOLOPF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PMKIFENPEBP(_message.Message):
    __slots__ = ("BDALEDOAHFA", "DJMCHFPIFLM", "OFNOGJPGBNA", "BHGDNCIOJDJ", "EJNINFFFKJP")
    BDALEDOAHFA_FIELD_NUMBER: _ClassVar[int]
    DJMCHFPIFLM_FIELD_NUMBER: _ClassVar[int]
    OFNOGJPGBNA_FIELD_NUMBER: _ClassVar[int]
    BHGDNCIOJDJ_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    BDALEDOAHFA: _NGOFPEOLOPF_pb2.NGOFPEOLOPF
    DJMCHFPIFLM: _containers.RepeatedCompositeFieldContainer[_NGOFPEOLOPF_pb2.NGOFPEOLOPF]
    OFNOGJPGBNA: int
    BHGDNCIOJDJ: int
    EJNINFFFKJP: int
    def __init__(self, BDALEDOAHFA: _Optional[_Union[_NGOFPEOLOPF_pb2.NGOFPEOLOPF, _Mapping]] = ..., DJMCHFPIFLM: _Optional[_Iterable[_Union[_NGOFPEOLOPF_pb2.NGOFPEOLOPF, _Mapping]]] = ..., OFNOGJPGBNA: _Optional[int] = ..., BHGDNCIOJDJ: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
