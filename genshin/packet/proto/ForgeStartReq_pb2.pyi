from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ForgeStartReq(_message.Message):
    __slots__ = ("avatar_id", "forge_count", "forge_id")
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    FORGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FORGE_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_id: int
    forge_count: int
    forge_id: int
    def __init__(self, avatar_id: _Optional[int] = ..., forge_count: _Optional[int] = ..., forge_id: _Optional[int] = ...) -> None: ...
