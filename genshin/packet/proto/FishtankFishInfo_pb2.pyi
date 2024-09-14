from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FishtankFishInfo(_message.Message):
    __slots__ = ("fish_distance_from_water", "fish_scale", "initial_rotation_y")
    FISH_DISTANCE_FROM_WATER_FIELD_NUMBER: _ClassVar[int]
    FISH_SCALE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_ROTATION_Y_FIELD_NUMBER: _ClassVar[int]
    fish_distance_from_water: float
    fish_scale: float
    initial_rotation_y: float
    def __init__(self, fish_distance_from_water: _Optional[float] = ..., fish_scale: _Optional[float] = ..., initial_rotation_y: _Optional[float] = ...) -> None: ...
