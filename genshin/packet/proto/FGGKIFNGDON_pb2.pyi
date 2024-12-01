from genshin.packet.proto import ENNOPJOFAJK_pb2 as _ENNOPJOFAJK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FGGKIFNGDON(_message.Message):
    __slots__ = ("MJAONINHIIB", "GAPODPGIELN", "CKKFFOLJCKH", "IIBIABPBBCO", "NIEKGOMDMOC", "JLDMENBIJDN")
    MJAONINHIIB_FIELD_NUMBER: _ClassVar[int]
    GAPODPGIELN_FIELD_NUMBER: _ClassVar[int]
    CKKFFOLJCKH_FIELD_NUMBER: _ClassVar[int]
    IIBIABPBBCO_FIELD_NUMBER: _ClassVar[int]
    NIEKGOMDMOC_FIELD_NUMBER: _ClassVar[int]
    JLDMENBIJDN_FIELD_NUMBER: _ClassVar[int]
    MJAONINHIIB: _containers.RepeatedScalarFieldContainer[int]
    GAPODPGIELN: _containers.RepeatedCompositeFieldContainer[_ENNOPJOFAJK_pb2.ENNOPJOFAJK]
    CKKFFOLJCKH: int
    IIBIABPBBCO: bool
    NIEKGOMDMOC: bool
    JLDMENBIJDN: int
    def __init__(self, MJAONINHIIB: _Optional[_Iterable[int]] = ..., GAPODPGIELN: _Optional[_Iterable[_Union[_ENNOPJOFAJK_pb2.ENNOPJOFAJK, _Mapping]]] = ..., CKKFFOLJCKH: _Optional[int] = ..., IIBIABPBBCO: bool = ..., NIEKGOMDMOC: bool = ..., JLDMENBIJDN: _Optional[int] = ...) -> None: ...
