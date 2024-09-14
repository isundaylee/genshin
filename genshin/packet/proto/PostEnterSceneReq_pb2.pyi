from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PostEnterSceneReq(_message.Message):
    __slots__ = ("total_tick_time", "enter_scene_token")
    TOTAL_TICK_TIME_FIELD_NUMBER: _ClassVar[int]
    ENTER_SCENE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    total_tick_time: float
    enter_scene_token: int
    def __init__(self, total_tick_time: _Optional[float] = ..., enter_scene_token: _Optional[int] = ...) -> None: ...
