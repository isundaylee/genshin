from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class StoreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    StoreType_STORE_NONE: _ClassVar[StoreType]
    StoreType_STORE_PACK: _ClassVar[StoreType]
    StoreType_STORE_DEPOT: _ClassVar[StoreType]
StoreType_STORE_NONE: StoreType
StoreType_STORE_PACK: StoreType
StoreType_STORE_DEPOT: StoreType
