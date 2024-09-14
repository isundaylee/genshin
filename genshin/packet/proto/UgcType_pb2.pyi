from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class UgcType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UGC_TYPE_NONE: _ClassVar[UgcType]
    UGC_TYPE_MUSIC_GAME: _ClassVar[UgcType]
UGC_TYPE_NONE: UgcType
UGC_TYPE_MUSIC_GAME: UgcType
