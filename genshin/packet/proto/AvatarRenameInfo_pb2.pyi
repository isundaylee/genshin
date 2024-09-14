from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarRenameInfo(_message.Message):
    __slots__ = ("avatar_id", "avatar_name")
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_NAME_FIELD_NUMBER: _ClassVar[int]
    avatar_id: int
    avatar_name: str
    def __init__(self, avatar_id: _Optional[int] = ..., avatar_name: _Optional[str] = ...) -> None: ...
