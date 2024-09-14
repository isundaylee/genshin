from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WeaponAwakenRsp(_message.Message):
    __slots__ = ("old_affix_level_map", "cur_affix_level_map", "retcode", "target_weapon_awaken_level", "target_weapon_guid", "avatar_guid")
    class OldAffixLevelMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class CurAffixLevelMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    OLD_AFFIX_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    CUR_AFFIX_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_WEAPON_AWAKEN_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TARGET_WEAPON_GUID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    old_affix_level_map: _containers.ScalarMap[int, int]
    cur_affix_level_map: _containers.ScalarMap[int, int]
    retcode: int
    target_weapon_awaken_level: int
    target_weapon_guid: int
    avatar_guid: int
    def __init__(self, old_affix_level_map: _Optional[_Mapping[int, int]] = ..., cur_affix_level_map: _Optional[_Mapping[int, int]] = ..., retcode: _Optional[int] = ..., target_weapon_awaken_level: _Optional[int] = ..., target_weapon_guid: _Optional[int] = ..., avatar_guid: _Optional[int] = ...) -> None: ...
