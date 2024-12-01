from genshin.packet.proto import OCBNHNOPDND_pb2 as _OCBNHNOPDND_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GPHNOOMOJPD(_message.Message):
    __slots__ = ("DNODMEKLBGH", "JEMBDAOOPHF", "DAJHKHFLNDJ")
    DNODMEKLBGH_FIELD_NUMBER: _ClassVar[int]
    JEMBDAOOPHF_FIELD_NUMBER: _ClassVar[int]
    DAJHKHFLNDJ_FIELD_NUMBER: _ClassVar[int]
    DNODMEKLBGH: _containers.RepeatedScalarFieldContainer[int]
    JEMBDAOOPHF: _containers.RepeatedCompositeFieldContainer[_OCBNHNOPDND_pb2.OCBNHNOPDND]
    DAJHKHFLNDJ: int
    def __init__(self, DNODMEKLBGH: _Optional[_Iterable[int]] = ..., JEMBDAOOPHF: _Optional[_Iterable[_Union[_OCBNHNOPDND_pb2.OCBNHNOPDND, _Mapping]]] = ..., DAJHKHFLNDJ: _Optional[int] = ...) -> None: ...
