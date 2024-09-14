from genshin.packet.proto import AbilitySyncStateInfo_pb2 as _AbilitySyncStateInfo_pb2
from genshin.packet.proto import ServerBuff_pb2 as _ServerBuff_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarEnterSceneInfo(_message.Message):
    __slots__ = ("weapon_entity_id", "weapon_ability_info", "avatar_entity_id", "weapon_guid", "server_buff_list", "avatar_ability_info", "buff_id_list", "avatar_guid")
    WEAPON_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    WEAPON_ABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    WEAPON_GUID_FIELD_NUMBER: _ClassVar[int]
    SERVER_BUFF_LIST_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    BUFF_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    weapon_entity_id: int
    weapon_ability_info: _AbilitySyncStateInfo_pb2.AbilitySyncStateInfo
    avatar_entity_id: int
    weapon_guid: int
    server_buff_list: _containers.RepeatedCompositeFieldContainer[_ServerBuff_pb2.ServerBuff]
    avatar_ability_info: _AbilitySyncStateInfo_pb2.AbilitySyncStateInfo
    buff_id_list: _containers.RepeatedScalarFieldContainer[int]
    avatar_guid: int
    def __init__(self, weapon_entity_id: _Optional[int] = ..., weapon_ability_info: _Optional[_Union[_AbilitySyncStateInfo_pb2.AbilitySyncStateInfo, _Mapping]] = ..., avatar_entity_id: _Optional[int] = ..., weapon_guid: _Optional[int] = ..., server_buff_list: _Optional[_Iterable[_Union[_ServerBuff_pb2.ServerBuff, _Mapping]]] = ..., avatar_ability_info: _Optional[_Union[_AbilitySyncStateInfo_pb2.AbilitySyncStateInfo, _Mapping]] = ..., buff_id_list: _Optional[_Iterable[int]] = ..., avatar_guid: _Optional[int] = ...) -> None: ...
