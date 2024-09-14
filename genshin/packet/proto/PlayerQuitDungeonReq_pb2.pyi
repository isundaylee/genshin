from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerQuitDungeonReq(_message.Message):
    __slots__ = ("point_id", "is_quit_immediately")
    POINT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_QUIT_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    point_id: int
    is_quit_immediately: bool
    def __init__(self, point_id: _Optional[int] = ..., is_quit_immediately: bool = ...) -> None: ...
