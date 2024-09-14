from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnchorPointData(_message.Message):
    __slots__ = ("scene_id", "end_time", "anchor_point_id", "pos", "rot")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    end_time: int
    anchor_point_id: int
    pos: _Vector_pb2.Vector
    rot: _Vector_pb2.Vector
    def __init__(self, scene_id: _Optional[int] = ..., end_time: _Optional[int] = ..., anchor_point_id: _Optional[int] = ..., pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
