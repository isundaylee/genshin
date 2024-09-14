from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterBornType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MONSTER_BORN_TYPE_NONE: _ClassVar[MonsterBornType]
    MONSTER_BORN_TYPE_DEFAULT: _ClassVar[MonsterBornType]
    MONSTER_BORN_TYPE_RANDOM: _ClassVar[MonsterBornType]
MONSTER_BORN_TYPE_NONE: MonsterBornType
MONSTER_BORN_TYPE_DEFAULT: MonsterBornType
MONSTER_BORN_TYPE_RANDOM: MonsterBornType
