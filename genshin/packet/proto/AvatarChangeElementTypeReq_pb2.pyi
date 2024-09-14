from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarChangeElementTypeReq(_message.Message):
    __slots__ = ("area_id", "scene_id")
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    area_id: int
    scene_id: int
    def __init__(self, area_id: _Optional[int] = ..., scene_id: _Optional[int] = ...) -> None: ...
