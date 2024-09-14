from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_INVALID: _ClassVar[State]
    STATE_IN_PROGRESS: _ClassVar[State]
    STATE_COMPLETE: _ClassVar[State]
    STATE_REWARD_TAKEN: _ClassVar[State]
STATE_INVALID: State
STATE_IN_PROGRESS: State
STATE_COMPLETE: State
STATE_REWARD_TAKEN: State
