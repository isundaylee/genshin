from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarUpgradeRsp(_message.Message):
    __slots__ = ("retcode", "old_level", "avatar_guid", "cur_level")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    OLD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    CUR_LEVEL_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    old_level: int
    avatar_guid: int
    cur_level: int
    def __init__(self, retcode: _Optional[int] = ..., old_level: _Optional[int] = ..., avatar_guid: _Optional[int] = ..., cur_level: _Optional[int] = ...) -> None: ...
