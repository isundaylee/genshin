from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HitColliderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HIT_COLLIDER_INVALID: _ClassVar[HitColliderType]
    HIT_COLLIDER_HIT_BOX: _ClassVar[HitColliderType]
    HIT_COLLIDER_WET_HIT_BOX: _ClassVar[HitColliderType]
    HIT_COLLIDER_HEAD_BOX: _ClassVar[HitColliderType]
HIT_COLLIDER_INVALID: HitColliderType
HIT_COLLIDER_HIT_BOX: HitColliderType
HIT_COLLIDER_WET_HIT_BOX: HitColliderType
HIT_COLLIDER_HEAD_BOX: HitColliderType
