from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeAnimalData(_message.Message):
    __slots__ = ("furniture_id", "spawn_pos", "spawn_rot")
    FURNITURE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAWN_POS_FIELD_NUMBER: _ClassVar[int]
    SPAWN_ROT_FIELD_NUMBER: _ClassVar[int]
    furniture_id: int
    spawn_pos: _Vector_pb2.Vector
    spawn_rot: _Vector_pb2.Vector
    def __init__(self, furniture_id: _Optional[int] = ..., spawn_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., spawn_rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
