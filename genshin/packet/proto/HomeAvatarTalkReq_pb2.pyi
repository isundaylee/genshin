from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeAvatarTalkReq(_message.Message):
    __slots__ = ("talk_id", "avatar_id")
    TALK_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    talk_id: int
    avatar_id: int
    def __init__(self, talk_id: _Optional[int] = ..., avatar_id: _Optional[int] = ...) -> None: ...
