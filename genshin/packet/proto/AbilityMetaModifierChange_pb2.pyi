from genshin.packet.proto import AbilityString_pb2 as _AbilityString_pb2
from genshin.packet.proto import ModifierProperty_pb2 as _ModifierProperty_pb2
from genshin.packet.proto import AbilityAttachedModifier_pb2 as _AbilityAttachedModifier_pb2
from genshin.packet.proto import ModifierAction_pb2 as _ModifierAction_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityMetaModifierChange(_message.Message):
    __slots__ = ("server_buff_uid", "parent_ability_override", "properties", "apply_entity_id", "attached_instanced_modifier", "parent_ability_name", "modifier_local_id", "is_attached_parent_ability", "EFONMKFIJNA", "MAPJDCOAIMG", "KKAAMMJBABH", "KKFHAIPCCFA", "action")
    SERVER_BUFF_UID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ABILITY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    APPLY_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_INSTANCED_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    PARENT_ABILITY_NAME_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ATTACHED_PARENT_ABILITY_FIELD_NUMBER: _ClassVar[int]
    EFONMKFIJNA_FIELD_NUMBER: _ClassVar[int]
    MAPJDCOAIMG_FIELD_NUMBER: _ClassVar[int]
    KKAAMMJBABH_FIELD_NUMBER: _ClassVar[int]
    KKFHAIPCCFA_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    server_buff_uid: int
    parent_ability_override: _AbilityString_pb2.AbilityString
    properties: _containers.RepeatedCompositeFieldContainer[_ModifierProperty_pb2.ModifierProperty]
    apply_entity_id: int
    attached_instanced_modifier: _AbilityAttachedModifier_pb2.AbilityAttachedModifier
    parent_ability_name: _AbilityString_pb2.AbilityString
    modifier_local_id: int
    is_attached_parent_ability: bool
    EFONMKFIJNA: bool
    MAPJDCOAIMG: bool
    KKAAMMJBABH: float
    KKFHAIPCCFA: int
    action: _ModifierAction_pb2.ModifierAction
    def __init__(self, server_buff_uid: _Optional[int] = ..., parent_ability_override: _Optional[_Union[_AbilityString_pb2.AbilityString, _Mapping]] = ..., properties: _Optional[_Iterable[_Union[_ModifierProperty_pb2.ModifierProperty, _Mapping]]] = ..., apply_entity_id: _Optional[int] = ..., attached_instanced_modifier: _Optional[_Union[_AbilityAttachedModifier_pb2.AbilityAttachedModifier, _Mapping]] = ..., parent_ability_name: _Optional[_Union[_AbilityString_pb2.AbilityString, _Mapping]] = ..., modifier_local_id: _Optional[int] = ..., is_attached_parent_ability: bool = ..., EFONMKFIJNA: bool = ..., MAPJDCOAIMG: bool = ..., KKAAMMJBABH: _Optional[float] = ..., KKFHAIPCCFA: _Optional[int] = ..., action: _Optional[_Union[_ModifierAction_pb2.ModifierAction, str]] = ...) -> None: ...
