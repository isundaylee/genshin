from genshin.packet.proto import IJJPJMEEPFI_pb2 as _IJJPJMEEPFI_pb2
from genshin.packet.proto import PropValue_pb2 as _PropValue_pb2
from genshin.packet.proto import TrialAvatarInfo_pb2 as _TrialAvatarInfo_pb2
from genshin.packet.proto import AvatarExcelInfo_pb2 as _AvatarExcelInfo_pb2
from genshin.packet.proto import AvatarEquipAffixInfo_pb2 as _AvatarEquipAffixInfo_pb2
from genshin.packet.proto import AvatarSkillInfo_pb2 as _AvatarSkillInfo_pb2
from genshin.packet.proto import AvatarFetterInfo_pb2 as _AvatarFetterInfo_pb2
from genshin.packet.proto import AvatarExpeditionState_pb2 as _AvatarExpeditionState_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarInfo(_message.Message):
    __slots__ = ("team_resonance_list", "HKEPBGNEHCN", "prop_map", "proud_skill_extra_level_map", "skill_level_map", "trial_avatar_info", "fight_prop_map", "excel_info", "talent_id_list", "equip_guid_list", "equip_affix_list", "skill_map", "fetter_info", "inherent_proud_skill_list", "pending_promote_reward_list", "is_focus", "PIHJHGKFCLH", "guid", "expedition_state", "born_time", "core_proud_skill_level", "costume_id", "anim_hash", "wearing_flycloak_id", "life_state", "DPMAABPLGDP", "MFMIPHLGDFL", "skill_depot_id", "avatar_type", "avatar_id")
    class PropMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _PropValue_pb2.PropValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_PropValue_pb2.PropValue, _Mapping]] = ...) -> None: ...
    class ProudSkillExtraLevelMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class SkillLevelMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
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
    TEAM_RESONANCE_LIST_FIELD_NUMBER: _ClassVar[int]
    HKEPBGNEHCN_FIELD_NUMBER: _ClassVar[int]
    PROP_MAP_FIELD_NUMBER: _ClassVar[int]
    PROUD_SKILL_EXTRA_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    TRIAL_AVATAR_INFO_FIELD_NUMBER: _ClassVar[int]
    FIGHT_PROP_MAP_FIELD_NUMBER: _ClassVar[int]
    EXCEL_INFO_FIELD_NUMBER: _ClassVar[int]
    TALENT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    EQUIP_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    EQUIP_AFFIX_LIST_FIELD_NUMBER: _ClassVar[int]
    SKILL_MAP_FIELD_NUMBER: _ClassVar[int]
    FETTER_INFO_FIELD_NUMBER: _ClassVar[int]
    INHERENT_PROUD_SKILL_LIST_FIELD_NUMBER: _ClassVar[int]
    PENDING_PROMOTE_REWARD_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_FOCUS_FIELD_NUMBER: _ClassVar[int]
    PIHJHGKFCLH_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    EXPEDITION_STATE_FIELD_NUMBER: _ClassVar[int]
    BORN_TIME_FIELD_NUMBER: _ClassVar[int]
    CORE_PROUD_SKILL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    ANIM_HASH_FIELD_NUMBER: _ClassVar[int]
    WEARING_FLYCLOAK_ID_FIELD_NUMBER: _ClassVar[int]
    LIFE_STATE_FIELD_NUMBER: _ClassVar[int]
    DPMAABPLGDP_FIELD_NUMBER: _ClassVar[int]
    MFMIPHLGDFL_FIELD_NUMBER: _ClassVar[int]
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    team_resonance_list: _containers.RepeatedScalarFieldContainer[int]
    HKEPBGNEHCN: _IJJPJMEEPFI_pb2.IJJPJMEEPFI
    prop_map: _containers.MessageMap[int, _PropValue_pb2.PropValue]
    proud_skill_extra_level_map: _containers.ScalarMap[int, int]
    skill_level_map: _containers.ScalarMap[int, int]
    trial_avatar_info: _TrialAvatarInfo_pb2.TrialAvatarInfo
    fight_prop_map: _containers.ScalarMap[int, float]
    excel_info: _AvatarExcelInfo_pb2.AvatarExcelInfo
    talent_id_list: _containers.RepeatedScalarFieldContainer[int]
    equip_guid_list: _containers.RepeatedScalarFieldContainer[int]
    equip_affix_list: _containers.RepeatedCompositeFieldContainer[_AvatarEquipAffixInfo_pb2.AvatarEquipAffixInfo]
    skill_map: _containers.MessageMap[int, _AvatarSkillInfo_pb2.AvatarSkillInfo]
    fetter_info: _AvatarFetterInfo_pb2.AvatarFetterInfo
    inherent_proud_skill_list: _containers.RepeatedScalarFieldContainer[int]
    pending_promote_reward_list: _containers.RepeatedScalarFieldContainer[int]
    is_focus: bool
    PIHJHGKFCLH: int
    guid: int
    expedition_state: _AvatarExpeditionState_pb2.AvatarExpeditionState
    born_time: int
    core_proud_skill_level: int
    costume_id: int
    anim_hash: int
    wearing_flycloak_id: int
    life_state: int
    DPMAABPLGDP: int
    MFMIPHLGDFL: int
    skill_depot_id: int
    avatar_type: int
    avatar_id: int
    def __init__(self, team_resonance_list: _Optional[_Iterable[int]] = ..., HKEPBGNEHCN: _Optional[_Union[_IJJPJMEEPFI_pb2.IJJPJMEEPFI, _Mapping]] = ..., prop_map: _Optional[_Mapping[int, _PropValue_pb2.PropValue]] = ..., proud_skill_extra_level_map: _Optional[_Mapping[int, int]] = ..., skill_level_map: _Optional[_Mapping[int, int]] = ..., trial_avatar_info: _Optional[_Union[_TrialAvatarInfo_pb2.TrialAvatarInfo, _Mapping]] = ..., fight_prop_map: _Optional[_Mapping[int, float]] = ..., excel_info: _Optional[_Union[_AvatarExcelInfo_pb2.AvatarExcelInfo, _Mapping]] = ..., talent_id_list: _Optional[_Iterable[int]] = ..., equip_guid_list: _Optional[_Iterable[int]] = ..., equip_affix_list: _Optional[_Iterable[_Union[_AvatarEquipAffixInfo_pb2.AvatarEquipAffixInfo, _Mapping]]] = ..., skill_map: _Optional[_Mapping[int, _AvatarSkillInfo_pb2.AvatarSkillInfo]] = ..., fetter_info: _Optional[_Union[_AvatarFetterInfo_pb2.AvatarFetterInfo, _Mapping]] = ..., inherent_proud_skill_list: _Optional[_Iterable[int]] = ..., pending_promote_reward_list: _Optional[_Iterable[int]] = ..., is_focus: bool = ..., PIHJHGKFCLH: _Optional[int] = ..., guid: _Optional[int] = ..., expedition_state: _Optional[_Union[_AvatarExpeditionState_pb2.AvatarExpeditionState, str]] = ..., born_time: _Optional[int] = ..., core_proud_skill_level: _Optional[int] = ..., costume_id: _Optional[int] = ..., anim_hash: _Optional[int] = ..., wearing_flycloak_id: _Optional[int] = ..., life_state: _Optional[int] = ..., DPMAABPLGDP: _Optional[int] = ..., MFMIPHLGDFL: _Optional[int] = ..., skill_depot_id: _Optional[int] = ..., avatar_type: _Optional[int] = ..., avatar_id: _Optional[int] = ...) -> None: ...
