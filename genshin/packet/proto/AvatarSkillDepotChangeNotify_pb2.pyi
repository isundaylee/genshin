from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarSkillDepotChangeNotify(_message.Message):
    __slots__ = ("entity_id", "core_proud_skill_level", "proud_skill_extra_level_map", "avatar_guid", "skill_level_map", "proud_skill_list", "talent_id_list", "skill_depot_id")
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
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CORE_PROUD_SKILL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PROUD_SKILL_EXTRA_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    PROUD_SKILL_LIST_FIELD_NUMBER: _ClassVar[int]
    TALENT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    core_proud_skill_level: int
    proud_skill_extra_level_map: _containers.ScalarMap[int, int]
    avatar_guid: int
    skill_level_map: _containers.ScalarMap[int, int]
    proud_skill_list: _containers.RepeatedScalarFieldContainer[int]
    talent_id_list: _containers.RepeatedScalarFieldContainer[int]
    skill_depot_id: int
    def __init__(self, entity_id: _Optional[int] = ..., core_proud_skill_level: _Optional[int] = ..., proud_skill_extra_level_map: _Optional[_Mapping[int, int]] = ..., avatar_guid: _Optional[int] = ..., skill_level_map: _Optional[_Mapping[int, int]] = ..., proud_skill_list: _Optional[_Iterable[int]] = ..., talent_id_list: _Optional[_Iterable[int]] = ..., skill_depot_id: _Optional[int] = ...) -> None: ...
