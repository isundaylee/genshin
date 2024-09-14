from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class StoreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORE_TYPE_NONE: _ClassVar[StoreType]
    STORE_TYPE_PACK: _ClassVar[StoreType]
    STORE_TYPE_DEPOT: _ClassVar[StoreType]
STORE_TYPE_NONE: StoreType
STORE_TYPE_PACK: StoreType
STORE_TYPE_DEPOT: StoreType
