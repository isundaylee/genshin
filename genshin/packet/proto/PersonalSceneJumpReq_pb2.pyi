from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PersonalSceneJumpReq(_message.Message):
    __slots__ = ("point_id",)
    POINT_ID_FIELD_NUMBER: _ClassVar[int]
    point_id: int
    def __init__(self, point_id: _Optional[int] = ...) -> None: ...
