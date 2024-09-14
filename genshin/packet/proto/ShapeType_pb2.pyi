from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ShapeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OBSTACLE_SHAPE_CAPSULE: _ClassVar[ShapeType]
    OBSTACLE_SHAPE_BOX: _ClassVar[ShapeType]
OBSTACLE_SHAPE_CAPSULE: ShapeType
OBSTACLE_SHAPE_BOX: ShapeType
