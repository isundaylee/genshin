from genshin.packet.proto import EODDBEANMOJ_pb2 as _EODDBEANMOJ_pb2
from genshin.packet.proto import DEEEIEGAKAD_pb2 as _DEEEIEGAKAD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BJOCDGNJEIB(_message.Message):
    __slots__ = ("CNAJAFLIBED", "GDGKAADBOGP", "FCDBBLEIACF", "GBNDPIFJBLI", "MPFLDFDOGAI", "NMIKCMLKNDM")
    CNAJAFLIBED_FIELD_NUMBER: _ClassVar[int]
    GDGKAADBOGP_FIELD_NUMBER: _ClassVar[int]
    FCDBBLEIACF_FIELD_NUMBER: _ClassVar[int]
    GBNDPIFJBLI_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    NMIKCMLKNDM_FIELD_NUMBER: _ClassVar[int]
    CNAJAFLIBED: _containers.RepeatedCompositeFieldContainer[_EODDBEANMOJ_pb2.EODDBEANMOJ]
    GDGKAADBOGP: _containers.RepeatedCompositeFieldContainer[_DEEEIEGAKAD_pb2.DEEEIEGAKAD]
    FCDBBLEIACF: int
    GBNDPIFJBLI: int
    MPFLDFDOGAI: bool
    NMIKCMLKNDM: int
    def __init__(self, CNAJAFLIBED: _Optional[_Iterable[_Union[_EODDBEANMOJ_pb2.EODDBEANMOJ, _Mapping]]] = ..., GDGKAADBOGP: _Optional[_Iterable[_Union[_DEEEIEGAKAD_pb2.DEEEIEGAKAD, _Mapping]]] = ..., FCDBBLEIACF: _Optional[int] = ..., GBNDPIFJBLI: _Optional[int] = ..., MPFLDFDOGAI: bool = ..., NMIKCMLKNDM: _Optional[int] = ...) -> None: ...
