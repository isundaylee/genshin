from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MILLGCOHBJI(_message.Message):
    __slots__ = ("MADGNDNLLEI", "BNHEAFCGIJM", "JFILODIHIPM", "OKDGOOAKCPA", "guid")
    MADGNDNLLEI_FIELD_NUMBER: _ClassVar[int]
    BNHEAFCGIJM_FIELD_NUMBER: _ClassVar[int]
    JFILODIHIPM_FIELD_NUMBER: _ClassVar[int]
    OKDGOOAKCPA_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    MADGNDNLLEI: _containers.RepeatedScalarFieldContainer[int]
    BNHEAFCGIJM: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    JFILODIHIPM: bool
    OKDGOOAKCPA: int
    guid: int
    def __init__(self, MADGNDNLLEI: _Optional[_Iterable[int]] = ..., BNHEAFCGIJM: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., JFILODIHIPM: bool = ..., OKDGOOAKCPA: _Optional[int] = ..., guid: _Optional[int] = ...) -> None: ...