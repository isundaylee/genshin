from genshin.packet.proto import ServerBuff_pb2 as _ServerBuff_pb2
from genshin.packet.proto import AvatarInfo_pb2 as _AvatarInfo_pb2
from genshin.packet.proto import SceneEntityInfo_pb2 as _SceneEntityInfo_pb2
from genshin.packet.proto import AbilityControlBlock_pb2 as _AbilityControlBlock_pb2
from genshin.packet.proto import AbilitySyncStateInfo_pb2 as _AbilitySyncStateInfo_pb2
from genshin.packet.proto import SceneAvatarInfo_pb2 as _SceneAvatarInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneTeamAvatar(_message.Message):
    __slots__ = ("is_reconnect", "scene_id", "server_buff_list", "avatar_info", "scene_entity_info", "weapon_entity_id", "player_uid", "ability_control_block", "entity_id", "weapon_guid", "avatar_ability_info", "weapon_ability_info", "scene_avatar_info", "is_player_cur_avatar", "avatar_guid", "is_on_scene")
    IS_RECONNECT_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_BUFF_LIST_FIELD_NUMBER: _ClassVar[int]
    AVATAR_INFO_FIELD_NUMBER: _ClassVar[int]
    SCENE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    WEAPON_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_UID_FIELD_NUMBER: _ClassVar[int]
    ABILITY_CONTROL_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    WEAPON_GUID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    WEAPON_ABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    SCENE_AVATAR_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_PLAYER_CUR_AVATAR_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    IS_ON_SCENE_FIELD_NUMBER: _ClassVar[int]
    is_reconnect: bool
    scene_id: int
    server_buff_list: _containers.RepeatedCompositeFieldContainer[_ServerBuff_pb2.ServerBuff]
    avatar_info: _AvatarInfo_pb2.AvatarInfo
    scene_entity_info: _SceneEntityInfo_pb2.SceneEntityInfo
    weapon_entity_id: int
    player_uid: int
    ability_control_block: _AbilityControlBlock_pb2.AbilityControlBlock
    entity_id: int
    weapon_guid: int
    avatar_ability_info: _AbilitySyncStateInfo_pb2.AbilitySyncStateInfo
    weapon_ability_info: _AbilitySyncStateInfo_pb2.AbilitySyncStateInfo
    scene_avatar_info: _SceneAvatarInfo_pb2.SceneAvatarInfo
    is_player_cur_avatar: bool
    avatar_guid: int
    is_on_scene: bool
    def __init__(self, is_reconnect: bool = ..., scene_id: _Optional[int] = ..., server_buff_list: _Optional[_Iterable[_Union[_ServerBuff_pb2.ServerBuff, _Mapping]]] = ..., avatar_info: _Optional[_Union[_AvatarInfo_pb2.AvatarInfo, _Mapping]] = ..., scene_entity_info: _Optional[_Union[_SceneEntityInfo_pb2.SceneEntityInfo, _Mapping]] = ..., weapon_entity_id: _Optional[int] = ..., player_uid: _Optional[int] = ..., ability_control_block: _Optional[_Union[_AbilityControlBlock_pb2.AbilityControlBlock, _Mapping]] = ..., entity_id: _Optional[int] = ..., weapon_guid: _Optional[int] = ..., avatar_ability_info: _Optional[_Union[_AbilitySyncStateInfo_pb2.AbilitySyncStateInfo, _Mapping]] = ..., weapon_ability_info: _Optional[_Union[_AbilitySyncStateInfo_pb2.AbilitySyncStateInfo, _Mapping]] = ..., scene_avatar_info: _Optional[_Union[_SceneAvatarInfo_pb2.SceneAvatarInfo, _Mapping]] = ..., is_player_cur_avatar: bool = ..., avatar_guid: _Optional[int] = ..., is_on_scene: bool = ...) -> None: ...
