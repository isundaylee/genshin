from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import HitColliderType_pb2 as _HitColliderType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HitCollision(_message.Message):
    __slots__ = ("DDLIENJBAKB", "hit_point", "hit_collider_type", "GGHMAHBOMKE", "EDOEECEACHH", "hit_box_index")
    DDLIENJBAKB_FIELD_NUMBER: _ClassVar[int]
    HIT_POINT_FIELD_NUMBER: _ClassVar[int]
    HIT_COLLIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    GGHMAHBOMKE_FIELD_NUMBER: _ClassVar[int]
    EDOEECEACHH_FIELD_NUMBER: _ClassVar[int]
    HIT_BOX_INDEX_FIELD_NUMBER: _ClassVar[int]
    DDLIENJBAKB: float
    hit_point: _Vector_pb2.Vector
    hit_collider_type: _HitColliderType_pb2.HitColliderType
    GGHMAHBOMKE: float
    EDOEECEACHH: _Vector_pb2.Vector
    hit_box_index: int
    def __init__(self, DDLIENJBAKB: _Optional[float] = ..., hit_point: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., hit_collider_type: _Optional[_Union[_HitColliderType_pb2.HitColliderType, str]] = ..., GGHMAHBOMKE: _Optional[float] = ..., EDOEECEACHH: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., hit_box_index: _Optional[int] = ...) -> None: ...
