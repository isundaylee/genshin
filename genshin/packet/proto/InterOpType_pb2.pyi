from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class InterOpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTER_OP_TYPE_FINISH: _ClassVar[InterOpType]
    INTER_OP_TYPE_START: _ClassVar[InterOpType]
INTER_OP_TYPE_FINISH: InterOpType
INTER_OP_TYPE_START: InterOpType
