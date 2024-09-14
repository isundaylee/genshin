from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProudSkillChangeNotify(_message.Message):
    __slots__ = ("skill_depot_id", "avatar_guid", "entity_id", "proud_skill_list")
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PROUD_SKILL_LIST_FIELD_NUMBER: _ClassVar[int]
    skill_depot_id: int
    avatar_guid: int
    entity_id: int
    proud_skill_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, skill_depot_id: _Optional[int] = ..., avatar_guid: _Optional[int] = ..., entity_id: _Optional[int] = ..., proud_skill_list: _Optional[_Iterable[int]] = ...) -> None: ...
