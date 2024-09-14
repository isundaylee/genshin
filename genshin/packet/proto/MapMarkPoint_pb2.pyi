from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import MapMarkPointType_pb2 as _MapMarkPointType_pb2
from genshin.packet.proto import MapMarkFromType_pb2 as _MapMarkFromType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapMarkPoint(_message.Message):
    __slots__ = ("scene_id", "name", "pos", "point_type", "monster_id", "from_type", "quest_id", "AGIENJJKPBE")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    POINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    AGIENJJKPBE_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    name: str
    pos: _Vector_pb2.Vector
    point_type: _MapMarkPointType_pb2.MapMarkPointType
    monster_id: int
    from_type: _MapMarkFromType_pb2.MapMarkFromType
    quest_id: int
    AGIENJJKPBE: int
    def __init__(self, scene_id: _Optional[int] = ..., name: _Optional[str] = ..., pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., point_type: _Optional[_Union[_MapMarkPointType_pb2.MapMarkPointType, str]] = ..., monster_id: _Optional[int] = ..., from_type: _Optional[_Union[_MapMarkFromType_pb2.MapMarkFromType, str]] = ..., quest_id: _Optional[int] = ..., AGIENJJKPBE: _Optional[int] = ...) -> None: ...
