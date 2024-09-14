from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class LockState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCK_NONE: _ClassVar[LockState]
    LOCK_QUEST: _ClassVar[LockState]
LOCK_NONE: LockState
LOCK_QUEST: LockState
