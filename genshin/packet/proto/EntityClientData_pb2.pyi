from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EntityClientData(_message.Message):
    __slots__ = ("wind_change_scene_time", "windmill_sync_angle", "wind_change_target_level")
    WIND_CHANGE_SCENE_TIME_FIELD_NUMBER: _ClassVar[int]
    WINDMILL_SYNC_ANGLE_FIELD_NUMBER: _ClassVar[int]
    WIND_CHANGE_TARGET_LEVEL_FIELD_NUMBER: _ClassVar[int]
    wind_change_scene_time: int
    windmill_sync_angle: float
    wind_change_target_level: int
    def __init__(self, wind_change_scene_time: _Optional[int] = ..., windmill_sync_angle: _Optional[float] = ..., wind_change_target_level: _Optional[int] = ...) -> None: ...
