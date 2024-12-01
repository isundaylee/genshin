from genshin.packet.proto import OHJPBJBAFNJ_pb2 as _OHJPBJBAFNJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HKBGIDACBIM(_message.Message):
    __slots__ = ("LLNPCEIFDBO", "HLMJFLEPCDO", "FMMPLGJNHMB")
    LLNPCEIFDBO_FIELD_NUMBER: _ClassVar[int]
    HLMJFLEPCDO_FIELD_NUMBER: _ClassVar[int]
    FMMPLGJNHMB_FIELD_NUMBER: _ClassVar[int]
    LLNPCEIFDBO: _containers.RepeatedScalarFieldContainer[int]
    HLMJFLEPCDO: _containers.RepeatedScalarFieldContainer[int]
    FMMPLGJNHMB: _OHJPBJBAFNJ_pb2.OHJPBJBAFNJ
    def __init__(self, LLNPCEIFDBO: _Optional[_Iterable[int]] = ..., HLMJFLEPCDO: _Optional[_Iterable[int]] = ..., FMMPLGJNHMB: _Optional[_Union[_OHJPBJBAFNJ_pb2.OHJPBJBAFNJ, str]] = ...) -> None: ...
