from genshin.packet.proto import HKHGFIHOKNC_pb2 as _HKHGFIHOKNC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HGCDBGCGOKI(_message.Message):
    __slots__ = ("EMFHFEGCJJB", "BFPMIHHHMIP", "ILNBDDPAKHP", "EJNINFFFKJP", "BPNKDCLMFOA", "GFBBGFPDMPJ")
    EMFHFEGCJJB_FIELD_NUMBER: _ClassVar[int]
    BFPMIHHHMIP_FIELD_NUMBER: _ClassVar[int]
    ILNBDDPAKHP_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    BPNKDCLMFOA_FIELD_NUMBER: _ClassVar[int]
    GFBBGFPDMPJ_FIELD_NUMBER: _ClassVar[int]
    EMFHFEGCJJB: _containers.RepeatedCompositeFieldContainer[_HKHGFIHOKNC_pb2.HKHGFIHOKNC]
    BFPMIHHHMIP: str
    ILNBDDPAKHP: bool
    EJNINFFFKJP: int
    BPNKDCLMFOA: int
    GFBBGFPDMPJ: int
    def __init__(self, EMFHFEGCJJB: _Optional[_Iterable[_Union[_HKHGFIHOKNC_pb2.HKHGFIHOKNC, _Mapping]]] = ..., BFPMIHHHMIP: _Optional[str] = ..., ILNBDDPAKHP: bool = ..., EJNINFFFKJP: _Optional[int] = ..., BPNKDCLMFOA: _Optional[int] = ..., GFBBGFPDMPJ: _Optional[int] = ...) -> None: ...
