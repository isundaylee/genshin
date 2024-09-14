from genshin.packet.proto import SceneWeaponInfo_pb2 as _SceneWeaponInfo_pb2
from genshin.packet.proto import SceneReliquaryInfo_pb2 as _SceneReliquaryInfo_pb2
from genshin.packet.proto import ServerBuff_pb2 as _ServerBuff_pb2
from genshin.packet.proto import CurVehicleInfo_pb2 as _CurVehicleInfo_pb2
from genshin.packet.proto import AvatarExcelInfo_pb2 as _AvatarExcelInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneAvatarInfo(_message.Message):
    __slots__ = ("uid", "avatar_id", "guid", "peer_id", "equip_id_list", "skill_depot_id", "talent_id_list", "weapon", "reliquary_list", "core_proud_skill_level", "inherent_proud_skill_list", "skill_level_map", "proud_skill_extra_level_map", "server_buff_list", "team_resonance_list", "wearing_flycloak_id", "born_time", "costume_id", "cur_vehicle_info", "excel_info", "anim_hash", "trace_effect_id")
    class SkillLevelMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ProudSkillExtraLevelMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    UID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    PEER_ID_FIELD_NUMBER: _ClassVar[int]
    EQUIP_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    TALENT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    RELIQUARY_LIST_FIELD_NUMBER: _ClassVar[int]
    CORE_PROUD_SKILL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    INHERENT_PROUD_SKILL_LIST_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    PROUD_SKILL_EXTRA_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    SERVER_BUFF_LIST_FIELD_NUMBER: _ClassVar[int]
    TEAM_RESONANCE_LIST_FIELD_NUMBER: _ClassVar[int]
    WEARING_FLYCLOAK_ID_FIELD_NUMBER: _ClassVar[int]
    BORN_TIME_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    CUR_VEHICLE_INFO_FIELD_NUMBER: _ClassVar[int]
    EXCEL_INFO_FIELD_NUMBER: _ClassVar[int]
    ANIM_HASH_FIELD_NUMBER: _ClassVar[int]
    TRACE_EFFECT_ID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    avatar_id: int
    guid: int
    peer_id: int
    equip_id_list: _containers.RepeatedScalarFieldContainer[int]
    skill_depot_id: int
    talent_id_list: _containers.RepeatedScalarFieldContainer[int]
    weapon: _SceneWeaponInfo_pb2.SceneWeaponInfo
    reliquary_list: _containers.RepeatedCompositeFieldContainer[_SceneReliquaryInfo_pb2.SceneReliquaryInfo]
    core_proud_skill_level: int
    inherent_proud_skill_list: _containers.RepeatedScalarFieldContainer[int]
    skill_level_map: _containers.ScalarMap[int, int]
    proud_skill_extra_level_map: _containers.ScalarMap[int, int]
    server_buff_list: _containers.RepeatedCompositeFieldContainer[_ServerBuff_pb2.ServerBuff]
    team_resonance_list: _containers.RepeatedScalarFieldContainer[int]
    wearing_flycloak_id: int
    born_time: int
    costume_id: int
    cur_vehicle_info: _CurVehicleInfo_pb2.CurVehicleInfo
    excel_info: _AvatarExcelInfo_pb2.AvatarExcelInfo
    anim_hash: int
    trace_effect_id: int
    def __init__(self, uid: _Optional[int] = ..., avatar_id: _Optional[int] = ..., guid: _Optional[int] = ..., peer_id: _Optional[int] = ..., equip_id_list: _Optional[_Iterable[int]] = ..., skill_depot_id: _Optional[int] = ..., talent_id_list: _Optional[_Iterable[int]] = ..., weapon: _Optional[_Union[_SceneWeaponInfo_pb2.SceneWeaponInfo, _Mapping]] = ..., reliquary_list: _Optional[_Iterable[_Union[_SceneReliquaryInfo_pb2.SceneReliquaryInfo, _Mapping]]] = ..., core_proud_skill_level: _Optional[int] = ..., inherent_proud_skill_list: _Optional[_Iterable[int]] = ..., skill_level_map: _Optional[_Mapping[int, int]] = ..., proud_skill_extra_level_map: _Optional[_Mapping[int, int]] = ..., server_buff_list: _Optional[_Iterable[_Union[_ServerBuff_pb2.ServerBuff, _Mapping]]] = ..., team_resonance_list: _Optional[_Iterable[int]] = ..., wearing_flycloak_id: _Optional[int] = ..., born_time: _Optional[int] = ..., costume_id: _Optional[int] = ..., cur_vehicle_info: _Optional[_Union[_CurVehicleInfo_pb2.CurVehicleInfo, _Mapping]] = ..., excel_info: _Optional[_Union[_AvatarExcelInfo_pb2.AvatarExcelInfo, _Mapping]] = ..., anim_hash: _Optional[int] = ..., trace_effect_id: _Optional[int] = ...) -> None: ...
