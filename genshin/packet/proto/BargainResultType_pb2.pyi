from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BargainResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BARGAIN_COMPLETE_SUCC: _ClassVar[BargainResultType]
    BARGAIN_SINGLE_FAIL: _ClassVar[BargainResultType]
    BARGAIN_COMPLETE_FAIL: _ClassVar[BargainResultType]
BARGAIN_COMPLETE_SUCC: BargainResultType
BARGAIN_SINGLE_FAIL: BargainResultType
BARGAIN_COMPLETE_FAIL: BargainResultType
