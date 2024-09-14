from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnlockAvatarTalentReq(_message.Message):
    __slots__ = ("avatar_guid", "talent_id")
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    TALENT_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_guid: int
    talent_id: int
    def __init__(self, avatar_guid: _Optional[int] = ..., talent_id: _Optional[int] = ...) -> None: ...
