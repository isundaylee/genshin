from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Investigation(_message.Message):
    __slots__ = ("id", "state", "total_progress", "progress")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID: _ClassVar[Investigation.State]
        IN_PROGRESS: _ClassVar[Investigation.State]
        COMPLETE: _ClassVar[Investigation.State]
        REWARD_TAKEN: _ClassVar[Investigation.State]
    INVALID: Investigation.State
    IN_PROGRESS: Investigation.State
    COMPLETE: Investigation.State
    REWARD_TAKEN: Investigation.State
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    state: Investigation.State
    total_progress: int
    progress: int
    def __init__(self, id: _Optional[int] = ..., state: _Optional[_Union[Investigation.State, str]] = ..., total_progress: _Optional[int] = ..., progress: _Optional[int] = ...) -> None: ...
