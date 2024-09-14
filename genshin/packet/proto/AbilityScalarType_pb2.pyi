from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityScalarType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ABILITY_SCALAR_TYPE_UNKNOW: _ClassVar[AbilityScalarType]
    ABILITY_SCALAR_TYPE_FLOAT: _ClassVar[AbilityScalarType]
    ABILITY_SCALAR_TYPE_INT: _ClassVar[AbilityScalarType]
    ABILITY_SCALAR_TYPE_BOOL: _ClassVar[AbilityScalarType]
    ABILITY_SCALAR_TYPE_TRIGGER: _ClassVar[AbilityScalarType]
    ABILITY_SCALAR_TYPE_STRING: _ClassVar[AbilityScalarType]
    ABILITY_SCALAR_TYPE_UINT: _ClassVar[AbilityScalarType]
ABILITY_SCALAR_TYPE_UNKNOW: AbilityScalarType
ABILITY_SCALAR_TYPE_FLOAT: AbilityScalarType
ABILITY_SCALAR_TYPE_INT: AbilityScalarType
ABILITY_SCALAR_TYPE_BOOL: AbilityScalarType
ABILITY_SCALAR_TYPE_TRIGGER: AbilityScalarType
ABILITY_SCALAR_TYPE_STRING: AbilityScalarType
ABILITY_SCALAR_TYPE_UINT: AbilityScalarType
