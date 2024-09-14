from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AiSkillCdInfo(_message.Message):
    __slots__ = ("skill_group_cd_map", "skill_cd_map")
    class SkillGroupCdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class SkillCdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    SKILL_GROUP_CD_MAP_FIELD_NUMBER: _ClassVar[int]
    SKILL_CD_MAP_FIELD_NUMBER: _ClassVar[int]
    skill_group_cd_map: _containers.ScalarMap[int, int]
    skill_cd_map: _containers.ScalarMap[int, int]
    def __init__(self, skill_group_cd_map: _Optional[_Mapping[int, int]] = ..., skill_cd_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
