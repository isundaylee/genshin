from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarSkillUpgradeRsp(_message.Message):
    __slots__ = ("old_level", "avatar_guid", "retcode", "cur_level", "avatar_skill_id")
    OLD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    CUR_LEVEL_FIELD_NUMBER: _ClassVar[int]
    AVATAR_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    old_level: int
    avatar_guid: int
    retcode: int
    cur_level: int
    avatar_skill_id: int
    def __init__(self, old_level: _Optional[int] = ..., avatar_guid: _Optional[int] = ..., retcode: _Optional[int] = ..., cur_level: _Optional[int] = ..., avatar_skill_id: _Optional[int] = ...) -> None: ...
