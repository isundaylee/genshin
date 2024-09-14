from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnlockAvatarTalentRsp(_message.Message):
    __slots__ = ("talent_id", "avatar_guid", "retcode")
    TALENT_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    talent_id: int
    avatar_guid: int
    retcode: int
    def __init__(self, talent_id: _Optional[int] = ..., avatar_guid: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
