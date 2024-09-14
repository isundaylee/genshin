from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarSkillMaxChargeCountNotify(_message.Message):
    __slots__ = ("skill_id", "max_charge_count", "avatar_guid")
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_CHARGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    skill_id: int
    max_charge_count: int
    avatar_guid: int
    def __init__(self, skill_id: _Optional[int] = ..., max_charge_count: _Optional[int] = ..., avatar_guid: _Optional[int] = ...) -> None: ...
