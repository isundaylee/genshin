from genshin.packet.proto import LFBOPOGGBPM_pb2 as _LFBOPOGGBPM_pb2
from genshin.packet.proto import BNGCIFIKLLO_pb2 as _BNGCIFIKLLO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OMHJKMMDJEO(_message.Message):
    __slots__ = ("KNJFLAJMAJJ", "PGEJGJMGGOG", "IGPHGEDLFLB")
    KNJFLAJMAJJ_FIELD_NUMBER: _ClassVar[int]
    PGEJGJMGGOG_FIELD_NUMBER: _ClassVar[int]
    IGPHGEDLFLB_FIELD_NUMBER: _ClassVar[int]
    KNJFLAJMAJJ: _containers.RepeatedScalarFieldContainer[int]
    PGEJGJMGGOG: _containers.RepeatedCompositeFieldContainer[_LFBOPOGGBPM_pb2.LFBOPOGGBPM]
    IGPHGEDLFLB: _containers.RepeatedCompositeFieldContainer[_BNGCIFIKLLO_pb2.BNGCIFIKLLO]
    def __init__(self, KNJFLAJMAJJ: _Optional[_Iterable[int]] = ..., PGEJGJMGGOG: _Optional[_Iterable[_Union[_LFBOPOGGBPM_pb2.LFBOPOGGBPM, _Mapping]]] = ..., IGPHGEDLFLB: _Optional[_Iterable[_Union[_BNGCIFIKLLO_pb2.BNGCIFIKLLO, _Mapping]]] = ...) -> None: ...
