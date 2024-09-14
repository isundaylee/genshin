from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SceneTimeNotify(_message.Message):
    __slots__ = ("scene_id", "scene_time", "is_paused")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    scene_time: int
    is_paused: bool
    def __init__(self, scene_id: _Optional[int] = ..., scene_time: _Optional[int] = ..., is_paused: bool = ...) -> None: ...
