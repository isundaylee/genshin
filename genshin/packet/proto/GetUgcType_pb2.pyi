from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class GetUgcType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GET_UGC_NONE: _ClassVar[GetUgcType]
    GET_UGC_TYPE_MINE: _ClassVar[GetUgcType]
    GET_UGC_TYPE_PUBLISH: _ClassVar[GetUgcType]
GET_UGC_NONE: GetUgcType
GET_UGC_TYPE_MINE: GetUgcType
GET_UGC_TYPE_PUBLISH: GetUgcType
