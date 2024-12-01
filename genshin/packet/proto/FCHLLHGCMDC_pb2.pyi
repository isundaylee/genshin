from genshin.packet.proto import NEOALIIGKHO_pb2 as _NEOALIIGKHO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FCHLLHGCMDC(_message.Message):
    __slots__ = ("BENGMPAKAMD", "HNECOEKKPAC", "anim_hash", "CPBNNCIFKDF", "KDBLFALMNEH", "GFPEPGGLPCM")
    BENGMPAKAMD_FIELD_NUMBER: _ClassVar[int]
    HNECOEKKPAC_FIELD_NUMBER: _ClassVar[int]
    ANIM_HASH_FIELD_NUMBER: _ClassVar[int]
    CPBNNCIFKDF_FIELD_NUMBER: _ClassVar[int]
    KDBLFALMNEH_FIELD_NUMBER: _ClassVar[int]
    GFPEPGGLPCM_FIELD_NUMBER: _ClassVar[int]
    BENGMPAKAMD: _containers.RepeatedCompositeFieldContainer[_NEOALIIGKHO_pb2.NEOALIIGKHO]
    HNECOEKKPAC: float
    anim_hash: int
    CPBNNCIFKDF: int
    KDBLFALMNEH: float
    GFPEPGGLPCM: int
    def __init__(self, BENGMPAKAMD: _Optional[_Iterable[_Union[_NEOALIIGKHO_pb2.NEOALIIGKHO, _Mapping]]] = ..., HNECOEKKPAC: _Optional[float] = ..., anim_hash: _Optional[int] = ..., CPBNNCIFKDF: _Optional[int] = ..., KDBLFALMNEH: _Optional[float] = ..., GFPEPGGLPCM: _Optional[int] = ...) -> None: ...
