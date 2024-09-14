from genshin.packet.proto import SceneWeaponInfo_pb2 as _SceneWeaponInfo_pb2
from genshin.packet.proto import MonsterBornType_pb2 as _MonsterBornType_pb2
from genshin.packet.proto import MonsterRoute_pb2 as _MonsterRoute_pb2
from genshin.packet.proto import SceneFishInfo_pb2 as _SceneFishInfo_pb2
from genshin.packet.proto import FishtankFishInfo_pb2 as _FishtankFishInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneMonsterInfo(_message.Message):
    __slots__ = ("monster_id", "group_id", "config_id", "weapon_list", "authority_peer_id", "affix_list", "is_elite", "owner_entity_id", "summoned_tag", "summon_tag_map", "pose_id", "born_type", "block_id", "mark_flag", "title_id", "special_name_id", "attack_target_id", "monster_route", "ai_config_id", "level_route_id", "init_pose_id", "is_light", "kill_num", "fish_info", "fishtank_fish_info")
    class SummonTagMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    WEAPON_LIST_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_PEER_ID_FIELD_NUMBER: _ClassVar[int]
    AFFIX_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_ELITE_FIELD_NUMBER: _ClassVar[int]
    OWNER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SUMMONED_TAG_FIELD_NUMBER: _ClassVar[int]
    SUMMON_TAG_MAP_FIELD_NUMBER: _ClassVar[int]
    POSE_ID_FIELD_NUMBER: _ClassVar[int]
    BORN_TYPE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    MARK_FLAG_FIELD_NUMBER: _ClassVar[int]
    TITLE_ID_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_NAME_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACK_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    MONSTER_ROUTE_FIELD_NUMBER: _ClassVar[int]
    AI_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_ROUTE_ID_FIELD_NUMBER: _ClassVar[int]
    INIT_POSE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_LIGHT_FIELD_NUMBER: _ClassVar[int]
    KILL_NUM_FIELD_NUMBER: _ClassVar[int]
    FISH_INFO_FIELD_NUMBER: _ClassVar[int]
    FISHTANK_FISH_INFO_FIELD_NUMBER: _ClassVar[int]
    monster_id: int
    group_id: int
    config_id: int
    weapon_list: _containers.RepeatedCompositeFieldContainer[_SceneWeaponInfo_pb2.SceneWeaponInfo]
    authority_peer_id: int
    affix_list: _containers.RepeatedScalarFieldContainer[int]
    is_elite: bool
    owner_entity_id: int
    summoned_tag: int
    summon_tag_map: _containers.ScalarMap[int, int]
    pose_id: int
    born_type: _MonsterBornType_pb2.MonsterBornType
    block_id: int
    mark_flag: int
    title_id: int
    special_name_id: int
    attack_target_id: int
    monster_route: _MonsterRoute_pb2.MonsterRoute
    ai_config_id: int
    level_route_id: int
    init_pose_id: int
    is_light: bool
    kill_num: int
    fish_info: _SceneFishInfo_pb2.SceneFishInfo
    fishtank_fish_info: _FishtankFishInfo_pb2.FishtankFishInfo
    def __init__(self, monster_id: _Optional[int] = ..., group_id: _Optional[int] = ..., config_id: _Optional[int] = ..., weapon_list: _Optional[_Iterable[_Union[_SceneWeaponInfo_pb2.SceneWeaponInfo, _Mapping]]] = ..., authority_peer_id: _Optional[int] = ..., affix_list: _Optional[_Iterable[int]] = ..., is_elite: bool = ..., owner_entity_id: _Optional[int] = ..., summoned_tag: _Optional[int] = ..., summon_tag_map: _Optional[_Mapping[int, int]] = ..., pose_id: _Optional[int] = ..., born_type: _Optional[_Union[_MonsterBornType_pb2.MonsterBornType, str]] = ..., block_id: _Optional[int] = ..., mark_flag: _Optional[int] = ..., title_id: _Optional[int] = ..., special_name_id: _Optional[int] = ..., attack_target_id: _Optional[int] = ..., monster_route: _Optional[_Union[_MonsterRoute_pb2.MonsterRoute, _Mapping]] = ..., ai_config_id: _Optional[int] = ..., level_route_id: _Optional[int] = ..., init_pose_id: _Optional[int] = ..., is_light: bool = ..., kill_num: _Optional[int] = ..., fish_info: _Optional[_Union[_SceneFishInfo_pb2.SceneFishInfo, _Mapping]] = ..., fishtank_fish_info: _Optional[_Union[_FishtankFishInfo_pb2.FishtankFishInfo, _Mapping]] = ...) -> None: ...
