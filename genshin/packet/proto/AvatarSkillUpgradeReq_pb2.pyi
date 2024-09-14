from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarSkillUpgradeReq(_message.Message):
    __slots__ = ("avatar_guid", "old_level", "avatar_skill_id")
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    OLD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    AVATAR_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_guid: int
    old_level: int
    avatar_skill_id: int
    def __init__(self, avatar_guid: _Optional[int] = ..., old_level: _Optional[int] = ..., avatar_skill_id: _Optional[int] = ...) -> None: ...
