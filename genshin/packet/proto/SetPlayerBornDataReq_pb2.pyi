from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPlayerBornDataReq(_message.Message):
    __slots__ = ("nick_name", "avatar_id")
    NICK_NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    nick_name: str
    avatar_id: int
    def __init__(self, nick_name: _Optional[str] = ..., avatar_id: _Optional[int] = ...) -> None: ...
