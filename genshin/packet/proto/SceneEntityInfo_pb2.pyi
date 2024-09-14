from genshin.packet.proto import ProtEntityType_pb2 as _ProtEntityType_pb2
from genshin.packet.proto import MotionInfo_pb2 as _MotionInfo_pb2
from genshin.packet.proto import PropPair_pb2 as _PropPair_pb2
from genshin.packet.proto import FightPropPair_pb2 as _FightPropPair_pb2
from genshin.packet.proto import AnimatorParameterValueInfoPair_pb2 as _AnimatorParameterValueInfoPair_pb2
from genshin.packet.proto import EntityClientData_pb2 as _EntityClientData_pb2
from genshin.packet.proto import EntityEnvironmentInfo_pb2 as _EntityEnvironmentInfo_pb2
from genshin.packet.proto import EntityAuthorityInfo_pb2 as _EntityAuthorityInfo_pb2
from genshin.packet.proto import ServerBuff_pb2 as _ServerBuff_pb2
from genshin.packet.proto import SceneAvatarInfo_pb2 as _SceneAvatarInfo_pb2
from genshin.packet.proto import SceneMonsterInfo_pb2 as _SceneMonsterInfo_pb2
from genshin.packet.proto import SceneNpcInfo_pb2 as _SceneNpcInfo_pb2
from genshin.packet.proto import SceneGadgetInfo_pb2 as _SceneGadgetInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneEntityInfo(_message.Message):
    __slots__ = ("entity_type", "entity_id", "name", "motion_info", "prop_list", "fight_prop_list", "life_state", "animator_para_list", "last_move_scene_time_ms", "last_move_reliable_seq", "entity_client_data", "entity_environment_info_list", "entity_authority_info", "tag_list", "server_buff_list", "avatar", "monster", "npc", "gadget")
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MOTION_INFO_FIELD_NUMBER: _ClassVar[int]
    PROP_LIST_FIELD_NUMBER: _ClassVar[int]
    FIGHT_PROP_LIST_FIELD_NUMBER: _ClassVar[int]
    LIFE_STATE_FIELD_NUMBER: _ClassVar[int]
    ANIMATOR_PARA_LIST_FIELD_NUMBER: _ClassVar[int]
    LAST_MOVE_SCENE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_MOVE_RELIABLE_SEQ_FIELD_NUMBER: _ClassVar[int]
    ENTITY_CLIENT_DATA_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ENVIRONMENT_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    ENTITY_AUTHORITY_INFO_FIELD_NUMBER: _ClassVar[int]
    TAG_LIST_FIELD_NUMBER: _ClassVar[int]
    SERVER_BUFF_LIST_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    MONSTER_FIELD_NUMBER: _ClassVar[int]
    NPC_FIELD_NUMBER: _ClassVar[int]
    GADGET_FIELD_NUMBER: _ClassVar[int]
    entity_type: _ProtEntityType_pb2.ProtEntityType
    entity_id: int
    name: str
    motion_info: _MotionInfo_pb2.MotionInfo
    prop_list: _containers.RepeatedCompositeFieldContainer[_PropPair_pb2.PropPair]
    fight_prop_list: _containers.RepeatedCompositeFieldContainer[_FightPropPair_pb2.FightPropPair]
    life_state: int
    animator_para_list: _containers.RepeatedCompositeFieldContainer[_AnimatorParameterValueInfoPair_pb2.AnimatorParameterValueInfoPair]
    last_move_scene_time_ms: int
    last_move_reliable_seq: int
    entity_client_data: _EntityClientData_pb2.EntityClientData
    entity_environment_info_list: _containers.RepeatedCompositeFieldContainer[_EntityEnvironmentInfo_pb2.EntityEnvironmentInfo]
    entity_authority_info: _EntityAuthorityInfo_pb2.EntityAuthorityInfo
    tag_list: _containers.RepeatedScalarFieldContainer[str]
    server_buff_list: _containers.RepeatedCompositeFieldContainer[_ServerBuff_pb2.ServerBuff]
    avatar: _SceneAvatarInfo_pb2.SceneAvatarInfo
    monster: _SceneMonsterInfo_pb2.SceneMonsterInfo
    npc: _SceneNpcInfo_pb2.SceneNpcInfo
    gadget: _SceneGadgetInfo_pb2.SceneGadgetInfo
    def __init__(self, entity_type: _Optional[_Union[_ProtEntityType_pb2.ProtEntityType, str]] = ..., entity_id: _Optional[int] = ..., name: _Optional[str] = ..., motion_info: _Optional[_Union[_MotionInfo_pb2.MotionInfo, _Mapping]] = ..., prop_list: _Optional[_Iterable[_Union[_PropPair_pb2.PropPair, _Mapping]]] = ..., fight_prop_list: _Optional[_Iterable[_Union[_FightPropPair_pb2.FightPropPair, _Mapping]]] = ..., life_state: _Optional[int] = ..., animator_para_list: _Optional[_Iterable[_Union[_AnimatorParameterValueInfoPair_pb2.AnimatorParameterValueInfoPair, _Mapping]]] = ..., last_move_scene_time_ms: _Optional[int] = ..., last_move_reliable_seq: _Optional[int] = ..., entity_client_data: _Optional[_Union[_EntityClientData_pb2.EntityClientData, _Mapping]] = ..., entity_environment_info_list: _Optional[_Iterable[_Union[_EntityEnvironmentInfo_pb2.EntityEnvironmentInfo, _Mapping]]] = ..., entity_authority_info: _Optional[_Union[_EntityAuthorityInfo_pb2.EntityAuthorityInfo, _Mapping]] = ..., tag_list: _Optional[_Iterable[str]] = ..., server_buff_list: _Optional[_Iterable[_Union[_ServerBuff_pb2.ServerBuff, _Mapping]]] = ..., avatar: _Optional[_Union[_SceneAvatarInfo_pb2.SceneAvatarInfo, _Mapping]] = ..., monster: _Optional[_Union[_SceneMonsterInfo_pb2.SceneMonsterInfo, _Mapping]] = ..., npc: _Optional[_Union[_SceneNpcInfo_pb2.SceneNpcInfo, _Mapping]] = ..., gadget: _Optional[_Union[_SceneGadgetInfo_pb2.SceneGadgetInfo, _Mapping]] = ...) -> None: ...
