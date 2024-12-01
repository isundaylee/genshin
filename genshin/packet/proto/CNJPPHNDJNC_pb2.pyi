from genshin.packet.proto import JJNLLNIBIMM_pb2 as _JJNLLNIBIMM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CNJPPHNDJNC(_message.Message):
    __slots__ = ("MNOFIBCLODD", "EAPNELHCBLM", "AOCIJOGPAJP")
    MNOFIBCLODD_FIELD_NUMBER: _ClassVar[int]
    EAPNELHCBLM_FIELD_NUMBER: _ClassVar[int]
    AOCIJOGPAJP_FIELD_NUMBER: _ClassVar[int]
    MNOFIBCLODD: _containers.RepeatedScalarFieldContainer[int]
    EAPNELHCBLM: _containers.RepeatedCompositeFieldContainer[_JJNLLNIBIMM_pb2.JJNLLNIBIMM]
    AOCIJOGPAJP: int
    def __init__(self, MNOFIBCLODD: _Optional[_Iterable[int]] = ..., EAPNELHCBLM: _Optional[_Iterable[_Union[_JJNLLNIBIMM_pb2.JJNLLNIBIMM, _Mapping]]] = ..., AOCIJOGPAJP: _Optional[int] = ...) -> None: ...
