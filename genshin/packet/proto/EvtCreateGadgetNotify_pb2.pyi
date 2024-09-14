from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import AbilityString_pb2 as _AbilityString_pb2
from genshin.packet.proto import ForwardType_pb2 as _ForwardType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtCreateGadgetNotify(_message.Message):
    __slots__ = ("target_lock_point_index_list", "init_pos", "init_euler_angles", "target_entity_id_list", "ability_name", "target_lock_point_index", "forward_type", "is_peer_id_from_player", "is_async_load", "sight_group_with_owner", "is_true_life_time_by_owner", "entity_id", "room_id", "init_pose_id", "prop_owner_entity_id", "local_id", "target_entity_id", "camp_type", "camp_id", "LKHKMKMKMJC", "owner_entity_id", "config_id", "guid")
    TARGET_LOCK_POINT_INDEX_LIST_FIELD_NUMBER: _ClassVar[int]
    INIT_POS_FIELD_NUMBER: _ClassVar[int]
    INIT_EULER_ANGLES_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    ABILITY_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_LOCK_POINT_INDEX_FIELD_NUMBER: _ClassVar[int]
    FORWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PEER_ID_FROM_PLAYER_FIELD_NUMBER: _ClassVar[int]
    IS_ASYNC_LOAD_FIELD_NUMBER: _ClassVar[int]
    SIGHT_GROUP_WITH_OWNER_FIELD_NUMBER: _ClassVar[int]
    IS_TRUE_LIFE_TIME_BY_OWNER_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    INIT_POSE_ID_FIELD_NUMBER: _ClassVar[int]
    PROP_OWNER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CAMP_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMP_ID_FIELD_NUMBER: _ClassVar[int]
    LKHKMKMKMJC_FIELD_NUMBER: _ClassVar[int]
    OWNER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    target_lock_point_index_list: _containers.RepeatedScalarFieldContainer[int]
    init_pos: _Vector_pb2.Vector
    init_euler_angles: _Vector_pb2.Vector
    target_entity_id_list: _containers.RepeatedScalarFieldContainer[int]
    ability_name: _AbilityString_pb2.AbilityString
    target_lock_point_index: int
    forward_type: _ForwardType_pb2.ForwardType
    is_peer_id_from_player: bool
    is_async_load: bool
    sight_group_with_owner: bool
    is_true_life_time_by_owner: bool
    entity_id: int
    room_id: int
    init_pose_id: int
    prop_owner_entity_id: int
    local_id: int
    target_entity_id: int
    camp_type: int
    camp_id: int
    LKHKMKMKMJC: int
    owner_entity_id: int
    config_id: int
    guid: int
    def __init__(self, target_lock_point_index_list: _Optional[_Iterable[int]] = ..., init_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., init_euler_angles: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., target_entity_id_list: _Optional[_Iterable[int]] = ..., ability_name: _Optional[_Union[_AbilityString_pb2.AbilityString, _Mapping]] = ..., target_lock_point_index: _Optional[int] = ..., forward_type: _Optional[_Union[_ForwardType_pb2.ForwardType, str]] = ..., is_peer_id_from_player: bool = ..., is_async_load: bool = ..., sight_group_with_owner: bool = ..., is_true_life_time_by_owner: bool = ..., entity_id: _Optional[int] = ..., room_id: _Optional[int] = ..., init_pose_id: _Optional[int] = ..., prop_owner_entity_id: _Optional[int] = ..., local_id: _Optional[int] = ..., target_entity_id: _Optional[int] = ..., camp_type: _Optional[int] = ..., camp_id: _Optional[int] = ..., LKHKMKMKMJC: _Optional[int] = ..., owner_entity_id: _Optional[int] = ..., config_id: _Optional[int] = ..., guid: _Optional[int] = ...) -> None: ...
