from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarFetterLevelRewardRsp(_message.Message):
    __slots__ = ("fetter_level", "reward_id", "retcode", "avatar_guid")
    FETTER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    fetter_level: int
    reward_id: int
    retcode: int
    avatar_guid: int
    def __init__(self, fetter_level: _Optional[int] = ..., reward_id: _Optional[int] = ..., retcode: _Optional[int] = ..., avatar_guid: _Optional[int] = ...) -> None: ...
