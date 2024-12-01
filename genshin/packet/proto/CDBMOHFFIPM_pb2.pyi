from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CDBMOHFFIPM(_message.Message):
    __slots__ = ("GOHAGOHHGLK", "talent_id_list", "skill_level_map", "proud_skill_extra_level_map", "AGIDBEEINDE", "skill_depot_id", "core_proud_skill_level", "MEJLFKPFPGK")
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
    GOHAGOHHGLK_FIELD_NUMBER: _ClassVar[int]
    TALENT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    PROUD_SKILL_EXTRA_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    CORE_PROUD_SKILL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MEJLFKPFPGK_FIELD_NUMBER: _ClassVar[int]
    GOHAGOHHGLK: _containers.RepeatedScalarFieldContainer[int]
    talent_id_list: _containers.RepeatedScalarFieldContainer[int]
    skill_level_map: _containers.ScalarMap[int, int]
    proud_skill_extra_level_map: _containers.ScalarMap[int, int]
    AGIDBEEINDE: int
    skill_depot_id: int
    core_proud_skill_level: int
    MEJLFKPFPGK: int
    def __init__(self, GOHAGOHHGLK: _Optional[_Iterable[int]] = ..., talent_id_list: _Optional[_Iterable[int]] = ..., skill_level_map: _Optional[_Mapping[int, int]] = ..., proud_skill_extra_level_map: _Optional[_Mapping[int, int]] = ..., AGIDBEEINDE: _Optional[int] = ..., skill_depot_id: _Optional[int] = ..., core_proud_skill_level: _Optional[int] = ..., MEJLFKPFPGK: _Optional[int] = ...) -> None: ...
