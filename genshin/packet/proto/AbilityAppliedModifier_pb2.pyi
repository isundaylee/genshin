from genshin.packet.proto import AbilityString_pb2 as _AbilityString_pb2
from genshin.packet.proto import AbilityAttachedModifier_pb2 as _AbilityAttachedModifier_pb2
from genshin.packet.proto import ModifierDurability_pb2 as _ModifierDurability_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityAppliedModifier(_message.Message):
    __slots__ = ("modifier_local_id", "parent_ability_entity_id", "parent_ability_name", "parent_ability_override", "instanced_ability_id", "instanced_modifier_id", "exist_duration", "attached_instanced_modifier", "apply_entity_id", "is_attached_parent_ability", "modifier_durability", "sbuff_uid", "is_serverbuff_modifier", "NCEGKBANOBP")
    MODIFIER_LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ABILITY_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ABILITY_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_ABILITY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_MODIFIER_ID_FIELD_NUMBER: _ClassVar[int]
    EXIST_DURATION_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_INSTANCED_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    APPLY_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ATTACHED_PARENT_ABILITY_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_DURABILITY_FIELD_NUMBER: _ClassVar[int]
    SBUFF_UID_FIELD_NUMBER: _ClassVar[int]
    IS_SERVERBUFF_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    NCEGKBANOBP_FIELD_NUMBER: _ClassVar[int]
    modifier_local_id: int
    parent_ability_entity_id: int
    parent_ability_name: _AbilityString_pb2.AbilityString
    parent_ability_override: _AbilityString_pb2.AbilityString
    instanced_ability_id: int
    instanced_modifier_id: int
    exist_duration: float
    attached_instanced_modifier: _AbilityAttachedModifier_pb2.AbilityAttachedModifier
    apply_entity_id: int
    is_attached_parent_ability: bool
    modifier_durability: _ModifierDurability_pb2.ModifierDurability
    sbuff_uid: int
    is_serverbuff_modifier: bool
    NCEGKBANOBP: bool
    def __init__(self, modifier_local_id: _Optional[int] = ..., parent_ability_entity_id: _Optional[int] = ..., parent_ability_name: _Optional[_Union[_AbilityString_pb2.AbilityString, _Mapping]] = ..., parent_ability_override: _Optional[_Union[_AbilityString_pb2.AbilityString, _Mapping]] = ..., instanced_ability_id: _Optional[int] = ..., instanced_modifier_id: _Optional[int] = ..., exist_duration: _Optional[float] = ..., attached_instanced_modifier: _Optional[_Union[_AbilityAttachedModifier_pb2.AbilityAttachedModifier, _Mapping]] = ..., apply_entity_id: _Optional[int] = ..., is_attached_parent_ability: bool = ..., modifier_durability: _Optional[_Union[_ModifierDurability_pb2.ModifierDurability, _Mapping]] = ..., sbuff_uid: _Optional[int] = ..., is_serverbuff_modifier: bool = ..., NCEGKBANOBP: bool = ...) -> None: ...
