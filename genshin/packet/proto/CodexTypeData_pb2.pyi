from genshin.packet.proto import CodexType_pb2 as _CodexType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CodexTypeData(_message.Message):
    __slots__ = ("weapon_max_promote_level_map", "have_viewed_list", "codex_id_list", "type")
    class WeaponMaxPromoteLevelMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    WEAPON_MAX_PROMOTE_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    HAVE_VIEWED_LIST_FIELD_NUMBER: _ClassVar[int]
    CODEX_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    weapon_max_promote_level_map: _containers.ScalarMap[int, int]
    have_viewed_list: _containers.RepeatedScalarFieldContainer[bool]
    codex_id_list: _containers.RepeatedScalarFieldContainer[int]
    type: _CodexType_pb2.CodexType
    def __init__(self, weapon_max_promote_level_map: _Optional[_Mapping[int, int]] = ..., have_viewed_list: _Optional[_Iterable[bool]] = ..., codex_id_list: _Optional[_Iterable[int]] = ..., type: _Optional[_Union[_CodexType_pb2.CodexType, str]] = ...) -> None: ...
