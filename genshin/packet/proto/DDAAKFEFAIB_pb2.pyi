from genshin.packet.proto import IOHOEDHLMDD_pb2 as _IOHOEDHLMDD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DDAAKFEFAIB(_message.Message):
    __slots__ = ("DOIJACGKGIJ", "JALEAGGJOKF", "type", "MDMMNLEEMDF")
    DOIJACGKGIJ_FIELD_NUMBER: _ClassVar[int]
    JALEAGGJOKF_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MDMMNLEEMDF_FIELD_NUMBER: _ClassVar[int]
    DOIJACGKGIJ: _containers.RepeatedCompositeFieldContainer[_IOHOEDHLMDD_pb2.IOHOEDHLMDD]
    JALEAGGJOKF: int
    type: int
    MDMMNLEEMDF: int
    def __init__(self, DOIJACGKGIJ: _Optional[_Iterable[_Union[_IOHOEDHLMDD_pb2.IOHOEDHLMDD, _Mapping]]] = ..., JALEAGGJOKF: _Optional[int] = ..., type: _Optional[int] = ..., MDMMNLEEMDF: _Optional[int] = ...) -> None: ...
