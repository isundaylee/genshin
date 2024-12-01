from genshin.packet.proto import MLECMFLLOGC_pb2 as _MLECMFLLOGC_pb2
from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BNACFAENGGE(_message.Message):
    __slots__ = ("MPMEJIBKJEO", "EFAJIHMNOBK", "EIIBFFCNPOF", "IJLHLCLLENE", "MLCGLCOKKEG", "IANEBDKAMBM", "NFDKKMJKPHH", "LLOMLFJHALG")
    MPMEJIBKJEO_FIELD_NUMBER: _ClassVar[int]
    EFAJIHMNOBK_FIELD_NUMBER: _ClassVar[int]
    EIIBFFCNPOF_FIELD_NUMBER: _ClassVar[int]
    IJLHLCLLENE_FIELD_NUMBER: _ClassVar[int]
    MLCGLCOKKEG_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    NFDKKMJKPHH_FIELD_NUMBER: _ClassVar[int]
    LLOMLFJHALG_FIELD_NUMBER: _ClassVar[int]
    MPMEJIBKJEO: str
    EFAJIHMNOBK: str
    EIIBFFCNPOF: _containers.RepeatedCompositeFieldContainer[_MLECMFLLOGC_pb2.MLECMFLLOGC]
    IJLHLCLLENE: str
    MLCGLCOKKEG: _containers.RepeatedScalarFieldContainer[int]
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    NFDKKMJKPHH: _containers.RepeatedScalarFieldContainer[int]
    LLOMLFJHALG: int
    def __init__(self, MPMEJIBKJEO: _Optional[str] = ..., EFAJIHMNOBK: _Optional[str] = ..., EIIBFFCNPOF: _Optional[_Iterable[_Union[_MLECMFLLOGC_pb2.MLECMFLLOGC, _Mapping]]] = ..., IJLHLCLLENE: _Optional[str] = ..., MLCGLCOKKEG: _Optional[_Iterable[int]] = ..., IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., NFDKKMJKPHH: _Optional[_Iterable[int]] = ..., LLOMLFJHALG: _Optional[int] = ...) -> None: ...
