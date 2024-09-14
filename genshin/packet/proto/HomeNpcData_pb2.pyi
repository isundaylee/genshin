from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeNpcData(_message.Message):
    __slots__ = ("avatar_id", "spawn_pos", "costume_id", "spawn_rot")
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    SPAWN_POS_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    SPAWN_ROT_FIELD_NUMBER: _ClassVar[int]
    avatar_id: int
    spawn_pos: _Vector_pb2.Vector
    costume_id: int
    spawn_rot: _Vector_pb2.Vector
    def __init__(self, avatar_id: _Optional[int] = ..., spawn_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., costume_id: _Optional[int] = ..., spawn_rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
