from genshin.packet.proto import LFOBKBCNFIC_pb2 as _LFOBKBCNFIC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LFCDJFKIHMK(_message.Message):
    __slots__ = ("BMOKGMFEELH", "MCDOGIALDKP", "FFAANBKLBKH", "EJNINFFFKJP")
    BMOKGMFEELH_FIELD_NUMBER: _ClassVar[int]
    MCDOGIALDKP_FIELD_NUMBER: _ClassVar[int]
    FFAANBKLBKH_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    BMOKGMFEELH: _containers.RepeatedScalarFieldContainer[int]
    MCDOGIALDKP: _LFOBKBCNFIC_pb2.LFOBKBCNFIC
    FFAANBKLBKH: _containers.RepeatedScalarFieldContainer[int]
    EJNINFFFKJP: int
    def __init__(self, BMOKGMFEELH: _Optional[_Iterable[int]] = ..., MCDOGIALDKP: _Optional[_Union[_LFOBKBCNFIC_pb2.LFOBKBCNFIC, _Mapping]] = ..., FFAANBKLBKH: _Optional[_Iterable[int]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
