from genshin.packet.proto import AbilityString_pb2 as _AbilityString_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetailAbilityInfo(_message.Message):
    __slots__ = ("instanced_ability_id", "caster_id", "modifier_local_id", "local_id", "parent_ability_name", "instanced_modifier_id")
    INSTANCED_ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    CASTER_ID_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ABILITY_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_MODIFIER_ID_FIELD_NUMBER: _ClassVar[int]
    instanced_ability_id: int
    caster_id: int
    modifier_local_id: int
    local_id: int
    parent_ability_name: _AbilityString_pb2.AbilityString
    instanced_modifier_id: int
    def __init__(self, instanced_ability_id: _Optional[int] = ..., caster_id: _Optional[int] = ..., modifier_local_id: _Optional[int] = ..., local_id: _Optional[int] = ..., parent_ability_name: _Optional[_Union[_AbilityString_pb2.AbilityString, _Mapping]] = ..., instanced_modifier_id: _Optional[int] = ...) -> None: ...
