from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeAvatarRewardEventGetReq(_message.Message):
    __slots__ = ("event_id", "avatar_id")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    avatar_id: int
    def __init__(self, event_id: _Optional[int] = ..., avatar_id: _Optional[int] = ...) -> None: ...
