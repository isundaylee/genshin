from genshin.packet.proto import PlayerDieType_pb2 as _PlayerDieType_pb2
from genshin.packet.proto import StrengthenPointData_pb2 as _StrengthenPointData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonPlayerDieNotify(_message.Message):
    __slots__ = ("die_type", "revive_count", "wait_time", "dungeon_id", "murderer_entity_id", "strengthen_point_data_map", "GKHNLKAADNG", "monster_id", "gadget_id")
    class StrengthenPointDataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _StrengthenPointData_pb2.StrengthenPointData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_StrengthenPointData_pb2.StrengthenPointData, _Mapping]] = ...) -> None: ...
    DIE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REVIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    WAIT_TIME_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    MURDERER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    STRENGTHEN_POINT_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    GKHNLKAADNG_FIELD_NUMBER: _ClassVar[int]
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    die_type: _PlayerDieType_pb2.PlayerDieType
    revive_count: int
    wait_time: int
    dungeon_id: int
    murderer_entity_id: int
    strengthen_point_data_map: _containers.MessageMap[int, _StrengthenPointData_pb2.StrengthenPointData]
    GKHNLKAADNG: int
    monster_id: int
    gadget_id: int
    def __init__(self, die_type: _Optional[_Union[_PlayerDieType_pb2.PlayerDieType, str]] = ..., revive_count: _Optional[int] = ..., wait_time: _Optional[int] = ..., dungeon_id: _Optional[int] = ..., murderer_entity_id: _Optional[int] = ..., strengthen_point_data_map: _Optional[_Mapping[int, _StrengthenPointData_pb2.StrengthenPointData]] = ..., GKHNLKAADNG: _Optional[int] = ..., monster_id: _Optional[int] = ..., gadget_id: _Optional[int] = ...) -> None: ...
