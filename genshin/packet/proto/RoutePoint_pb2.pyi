from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import MathQuaternion_pb2 as _MathQuaternion_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoutePoint(_message.Message):
    __slots__ = ("position", "arrive_range", "has_reach_event", "velocity", "time", "rotation", "rotation_speed", "axis_speed")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ARRIVE_RANGE_FIELD_NUMBER: _ClassVar[int]
    HAS_REACH_EVENT_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    ROTATION_SPEED_FIELD_NUMBER: _ClassVar[int]
    AXIS_SPEED_FIELD_NUMBER: _ClassVar[int]
    position: _Vector_pb2.Vector
    arrive_range: float
    has_reach_event: bool
    velocity: float
    time: float
    rotation: _Vector_pb2.Vector
    rotation_speed: _MathQuaternion_pb2.MathQuaternion
    axis_speed: _MathQuaternion_pb2.MathQuaternion
    def __init__(self, position: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., arrive_range: _Optional[float] = ..., has_reach_event: bool = ..., velocity: _Optional[float] = ..., time: _Optional[float] = ..., rotation: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., rotation_speed: _Optional[_Union[_MathQuaternion_pb2.MathQuaternion, _Mapping]] = ..., axis_speed: _Optional[_Union[_MathQuaternion_pb2.MathQuaternion, _Mapping]] = ...) -> None: ...
