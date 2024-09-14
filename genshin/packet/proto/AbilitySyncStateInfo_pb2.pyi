from genshin.packet.proto import AbilityScalarValueEntry_pb2 as _AbilityScalarValueEntry_pb2
from genshin.packet.proto import AbilityAppliedAbility_pb2 as _AbilityAppliedAbility_pb2
from genshin.packet.proto import AbilityAppliedModifier_pb2 as _AbilityAppliedModifier_pb2
from genshin.packet.proto import AbilityMixinRecoverInfo_pb2 as _AbilityMixinRecoverInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AbilitySyncStateInfo(_message.Message):
    __slots__ = ("is_inited", "dynamic_value_map", "applied_abilities", "applied_modifiers", "mixin_recover_infos", "sgv_dynamic_value_map")
    IS_INITED_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_VALUE_MAP_FIELD_NUMBER: _ClassVar[int]
    APPLIED_ABILITIES_FIELD_NUMBER: _ClassVar[int]
    APPLIED_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    MIXIN_RECOVER_INFOS_FIELD_NUMBER: _ClassVar[int]
    SGV_DYNAMIC_VALUE_MAP_FIELD_NUMBER: _ClassVar[int]
    is_inited: bool
    dynamic_value_map: _containers.RepeatedCompositeFieldContainer[_AbilityScalarValueEntry_pb2.AbilityScalarValueEntry]
    applied_abilities: _containers.RepeatedCompositeFieldContainer[_AbilityAppliedAbility_pb2.AbilityAppliedAbility]
    applied_modifiers: _containers.RepeatedCompositeFieldContainer[_AbilityAppliedModifier_pb2.AbilityAppliedModifier]
    mixin_recover_infos: _containers.RepeatedCompositeFieldContainer[_AbilityMixinRecoverInfo_pb2.AbilityMixinRecoverInfo]
    sgv_dynamic_value_map: _containers.RepeatedCompositeFieldContainer[_AbilityScalarValueEntry_pb2.AbilityScalarValueEntry]
    def __init__(self, is_inited: bool = ..., dynamic_value_map: _Optional[_Iterable[_Union[_AbilityScalarValueEntry_pb2.AbilityScalarValueEntry, _Mapping]]] = ..., applied_abilities: _Optional[_Iterable[_Union[_AbilityAppliedAbility_pb2.AbilityAppliedAbility, _Mapping]]] = ..., applied_modifiers: _Optional[_Iterable[_Union[_AbilityAppliedModifier_pb2.AbilityAppliedModifier, _Mapping]]] = ..., mixin_recover_infos: _Optional[_Iterable[_Union[_AbilityMixinRecoverInfo_pb2.AbilityMixinRecoverInfo, _Mapping]]] = ..., sgv_dynamic_value_map: _Optional[_Iterable[_Union[_AbilityScalarValueEntry_pb2.AbilityScalarValueEntry, _Mapping]]] = ...) -> None: ...
