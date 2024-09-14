from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WeaponPromoteRsp(_message.Message):
    __slots__ = ("target_weapon_guid", "cur_promote_level", "retcode", "old_promote_level")
    TARGET_WEAPON_GUID_FIELD_NUMBER: _ClassVar[int]
    CUR_PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    OLD_PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    target_weapon_guid: int
    cur_promote_level: int
    retcode: int
    old_promote_level: int
    def __init__(self, target_weapon_guid: _Optional[int] = ..., cur_promote_level: _Optional[int] = ..., retcode: _Optional[int] = ..., old_promote_level: _Optional[int] = ...) -> None: ...
