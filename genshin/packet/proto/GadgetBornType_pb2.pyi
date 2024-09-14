from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class GadgetBornType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GADGET_BORN_TYPE_NONE: _ClassVar[GadgetBornType]
    GADGET_BORN_TYPE_IN_AIR: _ClassVar[GadgetBornType]
    GADGET_BORN_TYPE_PLAYER: _ClassVar[GadgetBornType]
    GADGET_BORN_TYPE_MONSTER_HIT: _ClassVar[GadgetBornType]
    GADGET_BORN_TYPE_MONSTER_DIE: _ClassVar[GadgetBornType]
    GADGET_BORN_TYPE_GADGET: _ClassVar[GadgetBornType]
    GADGET_BORN_TYPE_GROUND: _ClassVar[GadgetBornType]
GADGET_BORN_TYPE_NONE: GadgetBornType
GADGET_BORN_TYPE_IN_AIR: GadgetBornType
GADGET_BORN_TYPE_PLAYER: GadgetBornType
GADGET_BORN_TYPE_MONSTER_HIT: GadgetBornType
GADGET_BORN_TYPE_MONSTER_DIE: GadgetBornType
GADGET_BORN_TYPE_GADGET: GadgetBornType
GADGET_BORN_TYPE_GROUND: GadgetBornType
