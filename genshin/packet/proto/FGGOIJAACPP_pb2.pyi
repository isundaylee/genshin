from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FGGOIJAACPP(_message.Message):
    __slots__ = ("OCNAEJFMCAG", "level", "BJLLGBAPJKP", "EJNINFFFKJP", "ECIFINMNLND")
    OCNAEJFMCAG_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    BJLLGBAPJKP_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    ECIFINMNLND_FIELD_NUMBER: _ClassVar[int]
    OCNAEJFMCAG: _containers.RepeatedCompositeFieldContainer[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ]
    level: _containers.RepeatedScalarFieldContainer[int]
    BJLLGBAPJKP: _containers.RepeatedScalarFieldContainer[int]
    EJNINFFFKJP: int
    ECIFINMNLND: int
    def __init__(self, OCNAEJFMCAG: _Optional[_Iterable[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]]] = ..., level: _Optional[_Iterable[int]] = ..., BJLLGBAPJKP: _Optional[_Iterable[int]] = ..., EJNINFFFKJP: _Optional[int] = ..., ECIFINMNLND: _Optional[int] = ...) -> None: ...
