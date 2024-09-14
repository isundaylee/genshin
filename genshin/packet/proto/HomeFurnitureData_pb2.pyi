from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeFurnitureData(_message.Message):
    __slots__ = ("guid", "spawn_pos", "furniture_id", "version", "parent_furniture_index", "spawn_rot")
    GUID_FIELD_NUMBER: _ClassVar[int]
    SPAWN_POS_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PARENT_FURNITURE_INDEX_FIELD_NUMBER: _ClassVar[int]
    SPAWN_ROT_FIELD_NUMBER: _ClassVar[int]
    guid: int
    spawn_pos: _Vector_pb2.Vector
    furniture_id: int
    version: int
    parent_furniture_index: int
    spawn_rot: _Vector_pb2.Vector
    def __init__(self, guid: _Optional[int] = ..., spawn_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., furniture_id: _Optional[int] = ..., version: _Optional[int] = ..., parent_furniture_index: _Optional[int] = ..., spawn_rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
