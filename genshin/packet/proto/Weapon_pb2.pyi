from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Weapon(_message.Message):
    __slots__ = ("affix_map", "level", "promote_level", "exp", "JAFJMOBLENI")
    class AffixMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    AFFIX_MAP_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    JAFJMOBLENI_FIELD_NUMBER: _ClassVar[int]
    affix_map: _containers.ScalarMap[int, int]
    level: int
    promote_level: int
    exp: int
    JAFJMOBLENI: bool
    def __init__(self, affix_map: _Optional[_Mapping[int, int]] = ..., level: _Optional[int] = ..., promote_level: _Optional[int] = ..., exp: _Optional[int] = ..., JAFJMOBLENI: bool = ...) -> None: ...
