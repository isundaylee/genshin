from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CoopReward(_message.Message):
    __slots__ = ("id", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNLOCK: _ClassVar[CoopReward.State]
        STATE_LOCK: _ClassVar[CoopReward.State]
        STATE_TAKEN: _ClassVar[CoopReward.State]
    STATE_UNLOCK: CoopReward.State
    STATE_LOCK: CoopReward.State
    STATE_TAKEN: CoopReward.State
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    state: CoopReward.State
    def __init__(self, id: _Optional[int] = ..., state: _Optional[_Union[CoopReward.State, str]] = ...) -> None: ...
