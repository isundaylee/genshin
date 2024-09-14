from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeAvatarRewardEventInfo(_message.Message):
    __slots__ = ("avatar_id", "suite_id", "guid", "random_position", "event_id")
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    RANDOM_POSITION_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_id: int
    suite_id: int
    guid: int
    random_position: int
    event_id: int
    def __init__(self, avatar_id: _Optional[int] = ..., suite_id: _Optional[int] = ..., guid: _Optional[int] = ..., random_position: _Optional[int] = ..., event_id: _Optional[int] = ...) -> None: ...
