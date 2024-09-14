from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EnterTransPointRegionNotify(_message.Message):
    __slots__ = ("point_id", "scene_id")
    POINT_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    point_id: int
    scene_id: int
    def __init__(self, point_id: _Optional[int] = ..., scene_id: _Optional[int] = ...) -> None: ...
