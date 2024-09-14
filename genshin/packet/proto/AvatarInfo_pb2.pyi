from genshin.packet.proto import PropValue_pb2 as _PropValue_pb2
from genshin.packet.proto import TrialAvatarInfo_pb2 as _TrialAvatarInfo_pb2
from genshin.packet.proto import AvatarSkillInfo_pb2 as _AvatarSkillInfo_pb2
from genshin.packet.proto import AvatarFetterInfo_pb2 as _AvatarFetterInfo_pb2
from genshin.packet.proto import AvatarExpeditionState_pb2 as _AvatarExpeditionState_pb2
from genshin.packet.proto import AvatarEquipAffixInfo_pb2 as _AvatarEquipAffixInfo_pb2
from genshin.packet.proto import AvatarExcelInfo_pb2 as _AvatarExcelInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarInfo(_message.Message):
    __slots__ = ("avatar_id", "guid", "prop_map", "life_state", "equip_guid_list", "talent_id_list", "fight_prop_map", "trial_avatar_info", "skill_map", "skill_depot_id", "fetter_info", "core_proud_skill_level", "inherent_proud_skill_list", "skill_level_map", "expedition_state", "proud_skill_extra_level_map", "is_focus", "avatar_type", "team_resonance_list", "wearing_flycloak_id", "equip_affix_list", "born_time", "pending_promote_reward_list", "costume_id", "excel_info", "anim_hash", "ABLFJPMKKDA", "GCHGLANNHMC", "KCINBOMOIGL")
    class PropMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _PropValue_pb2.PropValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_PropValue_pb2.PropValue, _Mapping]] = ...) -> None: ...
    class FightPropMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    class SkillMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _AvatarSkillInfo_pb2.AvatarSkillInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_AvatarSkillInfo_pb2.AvatarSkillInfo, _Mapping]] = ...) -> None: ...
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
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    PROP_MAP_FIELD_NUMBER: _ClassVar[int]
    LIFE_STATE_FIELD_NUMBER: _ClassVar[int]
    EQUIP_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    TALENT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    FIGHT_PROP_MAP_FIELD_NUMBER: _ClassVar[int]
    TRIAL_AVATAR_INFO_FIELD_NUMBER: _ClassVar[int]
    SKILL_MAP_FIELD_NUMBER: _ClassVar[int]
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    FETTER_INFO_FIELD_NUMBER: _ClassVar[int]
    CORE_PROUD_SKILL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    INHERENT_PROUD_SKILL_LIST_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    EXPEDITION_STATE_FIELD_NUMBER: _ClassVar[int]
    PROUD_SKILL_EXTRA_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_FOCUS_FIELD_NUMBER: _ClassVar[int]
    AVATAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEAM_RESONANCE_LIST_FIELD_NUMBER: _ClassVar[int]
    WEARING_FLYCLOAK_ID_FIELD_NUMBER: _ClassVar[int]
    EQUIP_AFFIX_LIST_FIELD_NUMBER: _ClassVar[int]
    BORN_TIME_FIELD_NUMBER: _ClassVar[int]
    PENDING_PROMOTE_REWARD_LIST_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    EXCEL_INFO_FIELD_NUMBER: _ClassVar[int]
    ANIM_HASH_FIELD_NUMBER: _ClassVar[int]
    ABLFJPMKKDA_FIELD_NUMBER: _ClassVar[int]
    GCHGLANNHMC_FIELD_NUMBER: _ClassVar[int]
    KCINBOMOIGL_FIELD_NUMBER: _ClassVar[int]
    avatar_id: int
    guid: int
    prop_map: _containers.MessageMap[int, _PropValue_pb2.PropValue]
    life_state: int
    equip_guid_list: _containers.RepeatedScalarFieldContainer[int]
    talent_id_list: _containers.RepeatedScalarFieldContainer[int]
    fight_prop_map: _containers.ScalarMap[int, float]
    trial_avatar_info: _TrialAvatarInfo_pb2.TrialAvatarInfo
    skill_map: _containers.MessageMap[int, _AvatarSkillInfo_pb2.AvatarSkillInfo]
    skill_depot_id: int
    fetter_info: _AvatarFetterInfo_pb2.AvatarFetterInfo
    core_proud_skill_level: int
    inherent_proud_skill_list: _containers.RepeatedScalarFieldContainer[int]
    skill_level_map: _containers.ScalarMap[int, int]
    expedition_state: _AvatarExpeditionState_pb2.AvatarExpeditionState
    proud_skill_extra_level_map: _containers.ScalarMap[int, int]
    is_focus: bool
    avatar_type: int
    team_resonance_list: _containers.RepeatedScalarFieldContainer[int]
    wearing_flycloak_id: int
    equip_affix_list: _containers.RepeatedCompositeFieldContainer[_AvatarEquipAffixInfo_pb2.AvatarEquipAffixInfo]
    born_time: int
    pending_promote_reward_list: _containers.RepeatedScalarFieldContainer[int]
    costume_id: int
    excel_info: _AvatarExcelInfo_pb2.AvatarExcelInfo
    anim_hash: int
    ABLFJPMKKDA: int
    GCHGLANNHMC: int
    KCINBOMOIGL: int
    def __init__(self, avatar_id: _Optional[int] = ..., guid: _Optional[int] = ..., prop_map: _Optional[_Mapping[int, _PropValue_pb2.PropValue]] = ..., life_state: _Optional[int] = ..., equip_guid_list: _Optional[_Iterable[int]] = ..., talent_id_list: _Optional[_Iterable[int]] = ..., fight_prop_map: _Optional[_Mapping[int, float]] = ..., trial_avatar_info: _Optional[_Union[_TrialAvatarInfo_pb2.TrialAvatarInfo, _Mapping]] = ..., skill_map: _Optional[_Mapping[int, _AvatarSkillInfo_pb2.AvatarSkillInfo]] = ..., skill_depot_id: _Optional[int] = ..., fetter_info: _Optional[_Union[_AvatarFetterInfo_pb2.AvatarFetterInfo, _Mapping]] = ..., core_proud_skill_level: _Optional[int] = ..., inherent_proud_skill_list: _Optional[_Iterable[int]] = ..., skill_level_map: _Optional[_Mapping[int, int]] = ..., expedition_state: _Optional[_Union[_AvatarExpeditionState_pb2.AvatarExpeditionState, str]] = ..., proud_skill_extra_level_map: _Optional[_Mapping[int, int]] = ..., is_focus: bool = ..., avatar_type: _Optional[int] = ..., team_resonance_list: _Optional[_Iterable[int]] = ..., wearing_flycloak_id: _Optional[int] = ..., equip_affix_list: _Optional[_Iterable[_Union[_AvatarEquipAffixInfo_pb2.AvatarEquipAffixInfo, _Mapping]]] = ..., born_time: _Optional[int] = ..., pending_promote_reward_list: _Optional[_Iterable[int]] = ..., costume_id: _Optional[int] = ..., excel_info: _Optional[_Union[_AvatarExcelInfo_pb2.AvatarExcelInfo, _Mapping]] = ..., anim_hash: _Optional[int] = ..., ABLFJPMKKDA: _Optional[int] = ..., GCHGLANNHMC: _Optional[int] = ..., KCINBOMOIGL: _Optional[int] = ...) -> None: ...
