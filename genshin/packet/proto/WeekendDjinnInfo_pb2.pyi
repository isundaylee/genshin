from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeekendDjinnInfo(_message.Message):
    __slots__ = ("pos", "rot")
    POS_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    pos: _Vector_pb2.Vector
    rot: _Vector_pb2.Vector
    def __init__(self, pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
