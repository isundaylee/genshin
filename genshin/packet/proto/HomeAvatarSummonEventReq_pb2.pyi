from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeAvatarSummonEventReq(_message.Message):
    __slots__ = ("guid", "suit_id", "avatar_id")
    GUID_FIELD_NUMBER: _ClassVar[int]
    SUIT_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    guid: int
    suit_id: int
    avatar_id: int
    def __init__(self, guid: _Optional[int] = ..., suit_id: _Optional[int] = ..., avatar_id: _Optional[int] = ...) -> None: ...
