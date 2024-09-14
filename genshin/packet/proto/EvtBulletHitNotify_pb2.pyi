from genshin.packet.proto import HitColliderType_pb2 as _HitColliderType_pb2
from genshin.packet.proto import ForwardType_pb2 as _ForwardType_pb2
from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtBulletHitNotify(_message.Message):
    __slots__ = ("single_bullet_id", "forward_peer", "hit_box_index", "hit_collider_type", "entity_id", "forward_type", "hit_point", "hit_entity_id", "hit_pointhit_normal")
    SINGLE_BULLET_ID_FIELD_NUMBER: _ClassVar[int]
    FORWARD_PEER_FIELD_NUMBER: _ClassVar[int]
    HIT_BOX_INDEX_FIELD_NUMBER: _ClassVar[int]
    HIT_COLLIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FORWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    HIT_POINT_FIELD_NUMBER: _ClassVar[int]
    HIT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    HIT_POINTHIT_NORMAL_FIELD_NUMBER: _ClassVar[int]
    single_bullet_id: int
    forward_peer: int
    hit_box_index: int
    hit_collider_type: _HitColliderType_pb2.HitColliderType
    entity_id: int
    forward_type: _ForwardType_pb2.ForwardType
    hit_point: _Vector_pb2.Vector
    hit_entity_id: int
    hit_pointhit_normal: _Vector_pb2.Vector
    def __init__(self, single_bullet_id: _Optional[int] = ..., forward_peer: _Optional[int] = ..., hit_box_index: _Optional[int] = ..., hit_collider_type: _Optional[_Union[_HitColliderType_pb2.HitColliderType, str]] = ..., entity_id: _Optional[int] = ..., forward_type: _Optional[_Union[_ForwardType_pb2.ForwardType, str]] = ..., hit_point: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., hit_entity_id: _Optional[int] = ..., hit_pointhit_normal: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
