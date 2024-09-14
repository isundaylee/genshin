from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateVehicleReq(_message.Message):
    __slots__ = ("rot", "pos", "vehicle_id", "scene_point_id")
    ROT_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    rot: _Vector_pb2.Vector
    pos: _Vector_pb2.Vector
    vehicle_id: int
    scene_point_id: int
    def __init__(self, rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., vehicle_id: _Optional[int] = ..., scene_point_id: _Optional[int] = ...) -> None: ...
