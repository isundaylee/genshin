from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FoundationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOUNDATION_STATUS_NONE: _ClassVar[FoundationStatus]
    FOUNDATION_STATUS_INIT: _ClassVar[FoundationStatus]
    FOUNDATION_STATUS_BUILDING: _ClassVar[FoundationStatus]
    FOUNDATION_STATUS_BUILT: _ClassVar[FoundationStatus]
FOUNDATION_STATUS_NONE: FoundationStatus
FOUNDATION_STATUS_INIT: FoundationStatus
FOUNDATION_STATUS_BUILDING: FoundationStatus
FOUNDATION_STATUS_BUILT: FoundationStatus
