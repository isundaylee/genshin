from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarRenameInfo(_message.Message):
    __slots__ = ("HGLNCCJIEAG", "avatar_id")
    HGLNCCJIEAG_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    HGLNCCJIEAG: str
    avatar_id: int
    def __init__(self, HGLNCCJIEAG: _Optional[str] = ..., avatar_id: _Optional[int] = ...) -> None: ...
