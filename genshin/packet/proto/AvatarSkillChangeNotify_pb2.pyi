from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarSkillChangeNotify(_message.Message):
    __slots__ = ("skill_depot_id", "old_level", "avatar_skill_id", "cur_level", "entity_id", "avatar_guid")
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    OLD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    AVATAR_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    CUR_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    skill_depot_id: int
    old_level: int
    avatar_skill_id: int
    cur_level: int
    entity_id: int
    avatar_guid: int
    def __init__(self, skill_depot_id: _Optional[int] = ..., old_level: _Optional[int] = ..., avatar_skill_id: _Optional[int] = ..., cur_level: _Optional[int] = ..., entity_id: _Optional[int] = ..., avatar_guid: _Optional[int] = ...) -> None: ...
