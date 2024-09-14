from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Weapon(_message.Message):
    __slots__ = ("level", "exp", "promote_level", "affix_map", "HHLNNPOILDL")
    class AffixMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    AFFIX_MAP_FIELD_NUMBER: _ClassVar[int]
    HHLNNPOILDL_FIELD_NUMBER: _ClassVar[int]
    level: int
    exp: int
    promote_level: int
    affix_map: _containers.ScalarMap[int, int]
    HHLNNPOILDL: bool
    def __init__(self, level: _Optional[int] = ..., exp: _Optional[int] = ..., promote_level: _Optional[int] = ..., affix_map: _Optional[_Mapping[int, int]] = ..., HHLNNPOILDL: bool = ...) -> None: ...
