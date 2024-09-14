from genshin.packet.proto import AbilityIdentifier_pb2 as _AbilityIdentifier_pb2
from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import AttackHitEffectResult_pb2 as _AttackHitEffectResult_pb2
from genshin.packet.proto import HitCollision_pb2 as _HitCollision_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AttackResult(_message.Message):
    __slots__ = ("attacker_id", "damage", "hit_retreat_angle_compat", "defense_id", "ability_identifier", "IICFMJEJOBO", "is_crit", "resolved_dir", "BAABHEHFAPH", "element_type", "hit_eff_result", "anim_event_id", "hit_collision", "MPBEBAKODGF", "EBLEIGGLHLG", "element_amplify_rate", "element_durability_attenuation", "mute_element_hurt", "MFLNDGPEJOE", "damage_shield", "IFMINIBILFH", "JKGEMBOBALF", "EKJHPCHCMLF", "POAFAPLMPEB", "use_gadget_damage_action", "ELIFILCNKFD", "endure_delta", "FLPFBAFHGNN", "NMPEDJOPMMB", "is_resist_text", "GMNJEDPKNDE")
    ATTACKER_ID_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_FIELD_NUMBER: _ClassVar[int]
    HIT_RETREAT_ANGLE_COMPAT_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_ID_FIELD_NUMBER: _ClassVar[int]
    ABILITY_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    IICFMJEJOBO_FIELD_NUMBER: _ClassVar[int]
    IS_CRIT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DIR_FIELD_NUMBER: _ClassVar[int]
    BAABHEHFAPH_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    HIT_EFF_RESULT_FIELD_NUMBER: _ClassVar[int]
    ANIM_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    HIT_COLLISION_FIELD_NUMBER: _ClassVar[int]
    MPBEBAKODGF_FIELD_NUMBER: _ClassVar[int]
    EBLEIGGLHLG_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_AMPLIFY_RATE_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_DURABILITY_ATTENUATION_FIELD_NUMBER: _ClassVar[int]
    MUTE_ELEMENT_HURT_FIELD_NUMBER: _ClassVar[int]
    MFLNDGPEJOE_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_SHIELD_FIELD_NUMBER: _ClassVar[int]
    IFMINIBILFH_FIELD_NUMBER: _ClassVar[int]
    JKGEMBOBALF_FIELD_NUMBER: _ClassVar[int]
    EKJHPCHCMLF_FIELD_NUMBER: _ClassVar[int]
    POAFAPLMPEB_FIELD_NUMBER: _ClassVar[int]
    USE_GADGET_DAMAGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    ELIFILCNKFD_FIELD_NUMBER: _ClassVar[int]
    ENDURE_DELTA_FIELD_NUMBER: _ClassVar[int]
    FLPFBAFHGNN_FIELD_NUMBER: _ClassVar[int]
    NMPEDJOPMMB_FIELD_NUMBER: _ClassVar[int]
    IS_RESIST_TEXT_FIELD_NUMBER: _ClassVar[int]
    GMNJEDPKNDE_FIELD_NUMBER: _ClassVar[int]
    attacker_id: int
    damage: float
    hit_retreat_angle_compat: int
    defense_id: int
    ability_identifier: _AbilityIdentifier_pb2.AbilityIdentifier
    IICFMJEJOBO: int
    is_crit: bool
    resolved_dir: _Vector_pb2.Vector
    BAABHEHFAPH: int
    element_type: int
    hit_eff_result: _AttackHitEffectResult_pb2.AttackHitEffectResult
    anim_event_id: str
    hit_collision: _HitCollision_pb2.HitCollision
    MPBEBAKODGF: int
    EBLEIGGLHLG: int
    element_amplify_rate: float
    element_durability_attenuation: float
    mute_element_hurt: bool
    MFLNDGPEJOE: int
    damage_shield: float
    IFMINIBILFH: int
    JKGEMBOBALF: int
    EKJHPCHCMLF: int
    POAFAPLMPEB: int
    use_gadget_damage_action: bool
    ELIFILCNKFD: int
    endure_delta: float
    FLPFBAFHGNN: int
    NMPEDJOPMMB: int
    is_resist_text: bool
    GMNJEDPKNDE: int
    def __init__(self, attacker_id: _Optional[int] = ..., damage: _Optional[float] = ..., hit_retreat_angle_compat: _Optional[int] = ..., defense_id: _Optional[int] = ..., ability_identifier: _Optional[_Union[_AbilityIdentifier_pb2.AbilityIdentifier, _Mapping]] = ..., IICFMJEJOBO: _Optional[int] = ..., is_crit: bool = ..., resolved_dir: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., BAABHEHFAPH: _Optional[int] = ..., element_type: _Optional[int] = ..., hit_eff_result: _Optional[_Union[_AttackHitEffectResult_pb2.AttackHitEffectResult, _Mapping]] = ..., anim_event_id: _Optional[str] = ..., hit_collision: _Optional[_Union[_HitCollision_pb2.HitCollision, _Mapping]] = ..., MPBEBAKODGF: _Optional[int] = ..., EBLEIGGLHLG: _Optional[int] = ..., element_amplify_rate: _Optional[float] = ..., element_durability_attenuation: _Optional[float] = ..., mute_element_hurt: bool = ..., MFLNDGPEJOE: _Optional[int] = ..., damage_shield: _Optional[float] = ..., IFMINIBILFH: _Optional[int] = ..., JKGEMBOBALF: _Optional[int] = ..., EKJHPCHCMLF: _Optional[int] = ..., POAFAPLMPEB: _Optional[int] = ..., use_gadget_damage_action: bool = ..., ELIFILCNKFD: _Optional[int] = ..., endure_delta: _Optional[float] = ..., FLPFBAFHGNN: _Optional[int] = ..., NMPEDJOPMMB: _Optional[int] = ..., is_resist_text: bool = ..., GMNJEDPKNDE: _Optional[int] = ...) -> None: ...
