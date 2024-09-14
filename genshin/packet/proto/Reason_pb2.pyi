from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVALID: _ClassVar[Reason]
    ENTER: _ClassVar[Reason]
    LEAVE: _ClassVar[Reason]
INVALID: Reason
ENTER: Reason
LEAVE: Reason
