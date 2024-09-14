from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PathStatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PATH_STATUS_TYPE_FAIL: _ClassVar[PathStatusType]
    PATH_STATUS_TYPE_SUCC: _ClassVar[PathStatusType]
    PATH_STATUS_TYPE_PARTIAL: _ClassVar[PathStatusType]
PATH_STATUS_TYPE_FAIL: PathStatusType
PATH_STATUS_TYPE_SUCC: PathStatusType
PATH_STATUS_TYPE_PARTIAL: PathStatusType
