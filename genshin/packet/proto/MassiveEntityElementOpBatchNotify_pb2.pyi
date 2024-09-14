from genshin.packet.proto import ShapeSphere_pb2 as _ShapeSphere_pb2
from genshin.packet.proto import ShapeBox_pb2 as _ShapeBox_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MassiveEntityElementOpBatchNotify(_message.Message):
    __slots__ = ("op_idx", "user_id", "attacker_id", "entity_type", "attack_element_durability", "uk1", "uk2", "shape_sphere", "shape_box")
    OP_IDX_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACKER_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTACK_ELEMENT_DURABILITY_FIELD_NUMBER: _ClassVar[int]
    UK1_FIELD_NUMBER: _ClassVar[int]
    UK2_FIELD_NUMBER: _ClassVar[int]
    SHAPE_SPHERE_FIELD_NUMBER: _ClassVar[int]
    SHAPE_BOX_FIELD_NUMBER: _ClassVar[int]
    op_idx: int
    user_id: int
    attacker_id: int
    entity_type: int
    attack_element_durability: float
    uk1: int
    uk2: int
    shape_sphere: _ShapeSphere_pb2.ShapeSphere
    shape_box: _ShapeBox_pb2.ShapeBox
    def __init__(self, op_idx: _Optional[int] = ..., user_id: _Optional[int] = ..., attacker_id: _Optional[int] = ..., entity_type: _Optional[int] = ..., attack_element_durability: _Optional[float] = ..., uk1: _Optional[int] = ..., uk2: _Optional[int] = ..., shape_sphere: _Optional[_Union[_ShapeSphere_pb2.ShapeSphere, _Mapping]] = ..., shape_box: _Optional[_Union[_ShapeBox_pb2.ShapeBox, _Mapping]] = ...) -> None: ...
