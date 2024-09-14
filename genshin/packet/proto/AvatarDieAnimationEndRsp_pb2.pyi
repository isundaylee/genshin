from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarDieAnimationEndRsp(_message.Message):
    __slots__ = ("retcode", "die_guid", "skill_id")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    DIE_GUID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    die_guid: int
    skill_id: int
    def __init__(self, retcode: _Optional[int] = ..., die_guid: _Optional[int] = ..., skill_id: _Optional[int] = ...) -> None: ...
