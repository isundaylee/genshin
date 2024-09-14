from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarUnlockTalentNotify(_message.Message):
    __slots__ = ("avatar_guid", "skill_depot_id", "entity_id", "talent_id")
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TALENT_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_guid: int
    skill_depot_id: int
    entity_id: int
    talent_id: int
    def __init__(self, avatar_guid: _Optional[int] = ..., skill_depot_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., talent_id: _Optional[int] = ...) -> None: ...
