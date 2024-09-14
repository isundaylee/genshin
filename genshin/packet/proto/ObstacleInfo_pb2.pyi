from genshin.packet.proto import ShapeType_pb2 as _ShapeType_pb2
from genshin.packet.proto import MathQuaternion_pb2 as _MathQuaternion_pb2
from genshin.packet.proto import Vector3Int_pb2 as _Vector3Int_pb2
from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObstacleInfo(_message.Message):
    __slots__ = ("shape", "rotation", "extents", "obstacle_id", "center")
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    EXTENTS_FIELD_NUMBER: _ClassVar[int]
    OBSTACLE_ID_FIELD_NUMBER: _ClassVar[int]
    CENTER_FIELD_NUMBER: _ClassVar[int]
    shape: _ShapeType_pb2.ShapeType
    rotation: _MathQuaternion_pb2.MathQuaternion
    extents: _Vector3Int_pb2.Vector3Int
    obstacle_id: int
    center: _Vector_pb2.Vector
    def __init__(self, shape: _Optional[_Union[_ShapeType_pb2.ShapeType, str]] = ..., rotation: _Optional[_Union[_MathQuaternion_pb2.MathQuaternion, _Mapping]] = ..., extents: _Optional[_Union[_Vector3Int_pb2.Vector3Int, _Mapping]] = ..., obstacle_id: _Optional[int] = ..., center: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
