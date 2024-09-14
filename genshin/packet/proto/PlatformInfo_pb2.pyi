from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import MathQuaternion_pb2 as _MathQuaternion_pb2
from genshin.packet.proto import MovingPlatformType_pb2 as _MovingPlatformType_pb2
from genshin.packet.proto import Route_pb2 as _Route_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlatformInfo(_message.Message):
    __slots__ = ("route_id", "start_index", "start_route_time", "start_scene_time", "start_pos", "is_started", "start_rot", "stop_scene_time", "pos_offset", "rot_offset", "moving_platform_type", "is_active", "route", "point_id")
    ROUTE_ID_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    START_ROUTE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_SCENE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_POS_FIELD_NUMBER: _ClassVar[int]
    IS_STARTED_FIELD_NUMBER: _ClassVar[int]
    START_ROT_FIELD_NUMBER: _ClassVar[int]
    STOP_SCENE_TIME_FIELD_NUMBER: _ClassVar[int]
    POS_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ROT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    MOVING_PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    POINT_ID_FIELD_NUMBER: _ClassVar[int]
    route_id: int
    start_index: int
    start_route_time: int
    start_scene_time: int
    start_pos: _Vector_pb2.Vector
    is_started: bool
    start_rot: _MathQuaternion_pb2.MathQuaternion
    stop_scene_time: int
    pos_offset: _Vector_pb2.Vector
    rot_offset: _MathQuaternion_pb2.MathQuaternion
    moving_platform_type: _MovingPlatformType_pb2.MovingPlatformType
    is_active: bool
    route: _Route_pb2.Route
    point_id: int
    def __init__(self, route_id: _Optional[int] = ..., start_index: _Optional[int] = ..., start_route_time: _Optional[int] = ..., start_scene_time: _Optional[int] = ..., start_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., is_started: bool = ..., start_rot: _Optional[_Union[_MathQuaternion_pb2.MathQuaternion, _Mapping]] = ..., stop_scene_time: _Optional[int] = ..., pos_offset: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., rot_offset: _Optional[_Union[_MathQuaternion_pb2.MathQuaternion, _Mapping]] = ..., moving_platform_type: _Optional[_Union[_MovingPlatformType_pb2.MovingPlatformType, str]] = ..., is_active: bool = ..., route: _Optional[_Union[_Route_pb2.Route, _Mapping]] = ..., point_id: _Optional[int] = ...) -> None: ...
