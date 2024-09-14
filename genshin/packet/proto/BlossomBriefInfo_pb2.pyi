from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlossomBriefInfo(_message.Message):
    __slots__ = ("refresh_id", "resin", "monster_level", "reward_id", "is_guide_opened", "scene_id", "city_id", "map_layer_id", "pos", "state", "circle_camp_id")
    REFRESH_ID_FIELD_NUMBER: _ClassVar[int]
    RESIN_FIELD_NUMBER: _ClassVar[int]
    MONSTER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    IS_GUIDE_OPENED_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    CITY_ID_FIELD_NUMBER: _ClassVar[int]
    MAP_LAYER_ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CIRCLE_CAMP_ID_FIELD_NUMBER: _ClassVar[int]
    refresh_id: int
    resin: int
    monster_level: int
    reward_id: int
    is_guide_opened: bool
    scene_id: int
    city_id: int
    map_layer_id: int
    pos: _Vector_pb2.Vector
    state: int
    circle_camp_id: int
    def __init__(self, refresh_id: _Optional[int] = ..., resin: _Optional[int] = ..., monster_level: _Optional[int] = ..., reward_id: _Optional[int] = ..., is_guide_opened: bool = ..., scene_id: _Optional[int] = ..., city_id: _Optional[int] = ..., map_layer_id: _Optional[int] = ..., pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., state: _Optional[int] = ..., circle_camp_id: _Optional[int] = ...) -> None: ...
