from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterSummonTagNotify(_message.Message):
    __slots__ = ("summon_tag_map", "monster_entity_id")
    class SummonTagMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    SUMMON_TAG_MAP_FIELD_NUMBER: _ClassVar[int]
    MONSTER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    summon_tag_map: _containers.ScalarMap[int, int]
    monster_entity_id: int
    def __init__(self, summon_tag_map: _Optional[_Mapping[int, int]] = ..., monster_entity_id: _Optional[int] = ...) -> None: ...
