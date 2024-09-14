from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeAvatarSummonEventInfo(_message.Message):
    __slots__ = ("event_id", "guid", "event_over_time", "suit_id", "random_position", "avatar_id")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    EVENT_OVER_TIME_FIELD_NUMBER: _ClassVar[int]
    SUIT_ID_FIELD_NUMBER: _ClassVar[int]
    RANDOM_POSITION_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    guid: int
    event_over_time: int
    suit_id: int
    random_position: int
    avatar_id: int
    def __init__(self, event_id: _Optional[int] = ..., guid: _Optional[int] = ..., event_over_time: _Optional[int] = ..., suit_id: _Optional[int] = ..., random_position: _Optional[int] = ..., avatar_id: _Optional[int] = ...) -> None: ...
