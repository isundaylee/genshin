from genshin.packet.proto import CNJODFLJDIE_pb2 as _CNJODFLJDIE_pb2
from genshin.packet.proto import EGEKCOIJOLN_pb2 as _EGEKCOIJOLN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CLJABGNOJBH(_message.Message):
    __slots__ = ("GIPEPNIONAK", "MFOHCKAFFMM", "KCKEPCMLIHI", "OEJIPIOBDAI", "NMIKCMLKNDM", "MPFLDFDOGAI")
    GIPEPNIONAK_FIELD_NUMBER: _ClassVar[int]
    MFOHCKAFFMM_FIELD_NUMBER: _ClassVar[int]
    KCKEPCMLIHI_FIELD_NUMBER: _ClassVar[int]
    OEJIPIOBDAI_FIELD_NUMBER: _ClassVar[int]
    NMIKCMLKNDM_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    GIPEPNIONAK: _containers.RepeatedScalarFieldContainer[int]
    MFOHCKAFFMM: _containers.RepeatedCompositeFieldContainer[_CNJODFLJDIE_pb2.CNJODFLJDIE]
    KCKEPCMLIHI: _containers.RepeatedCompositeFieldContainer[_EGEKCOIJOLN_pb2.EGEKCOIJOLN]
    OEJIPIOBDAI: _containers.RepeatedScalarFieldContainer[int]
    NMIKCMLKNDM: int
    MPFLDFDOGAI: bool
    def __init__(self, GIPEPNIONAK: _Optional[_Iterable[int]] = ..., MFOHCKAFFMM: _Optional[_Iterable[_Union[_CNJODFLJDIE_pb2.CNJODFLJDIE, _Mapping]]] = ..., KCKEPCMLIHI: _Optional[_Iterable[_Union[_EGEKCOIJOLN_pb2.EGEKCOIJOLN, _Mapping]]] = ..., OEJIPIOBDAI: _Optional[_Iterable[int]] = ..., NMIKCMLKNDM: _Optional[int] = ..., MPFLDFDOGAI: bool = ...) -> None: ...
