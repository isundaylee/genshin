from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import MotionState_pb2 as _MotionState_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MotionInfo(_message.Message):
    __slots__ = ("pos", "rot", "speed", "state", "params", "ref_pos", "ref_id", "scene_time", "interval_velocity", "BIMCAJGDDOI", "HJCDICMBDKE")
    POS_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    REF_POS_FIELD_NUMBER: _ClassVar[int]
    REF_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_TIME_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    BIMCAJGDDOI_FIELD_NUMBER: _ClassVar[int]
    HJCDICMBDKE_FIELD_NUMBER: _ClassVar[int]
    pos: _Vector_pb2.Vector
    rot: _Vector_pb2.Vector
    speed: _Vector_pb2.Vector
    state: _MotionState_pb2.MotionState
    params: _containers.RepeatedCompositeFieldContainer[_Vector_pb2.Vector]
    ref_pos: _Vector_pb2.Vector
    ref_id: int
    scene_time: int
    interval_velocity: int
    BIMCAJGDDOI: int
    HJCDICMBDKE: int
    def __init__(self, pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., speed: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., state: _Optional[_Union[_MotionState_pb2.MotionState, str]] = ..., params: _Optional[_Iterable[_Union[_Vector_pb2.Vector, _Mapping]]] = ..., ref_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., ref_id: _Optional[int] = ..., scene_time: _Optional[int] = ..., interval_velocity: _Optional[int] = ..., BIMCAJGDDOI: _Optional[int] = ..., HJCDICMBDKE: _Optional[int] = ...) -> None: ...
