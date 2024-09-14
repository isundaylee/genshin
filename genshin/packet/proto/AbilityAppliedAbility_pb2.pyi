from genshin.packet.proto import AbilityString_pb2 as _AbilityString_pb2
from genshin.packet.proto import AbilityScalarValueEntry_pb2 as _AbilityScalarValueEntry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityAppliedAbility(_message.Message):
    __slots__ = ("ability_name", "ability_override", "override_map", "instanced_ability_id")
    ABILITY_NAME_FIELD_NUMBER: _ClassVar[int]
    ABILITY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_MAP_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    ability_name: _AbilityString_pb2.AbilityString
    ability_override: _AbilityString_pb2.AbilityString
    override_map: _containers.RepeatedCompositeFieldContainer[_AbilityScalarValueEntry_pb2.AbilityScalarValueEntry]
    instanced_ability_id: int
    def __init__(self, ability_name: _Optional[_Union[_AbilityString_pb2.AbilityString, _Mapping]] = ..., ability_override: _Optional[_Union[_AbilityString_pb2.AbilityString, _Mapping]] = ..., override_map: _Optional[_Iterable[_Union[_AbilityScalarValueEntry_pb2.AbilityScalarValueEntry, _Mapping]]] = ..., instanced_ability_id: _Optional[int] = ...) -> None: ...
