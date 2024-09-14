from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CoopPoint(_message.Message):
    __slots__ = ("id", "state", "self_confidence")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSTARTED: _ClassVar[CoopPoint.State]
        STATE_STARTED: _ClassVar[CoopPoint.State]
        STATE_FINISHED: _ClassVar[CoopPoint.State]
    STATE_UNSTARTED: CoopPoint.State
    STATE_STARTED: CoopPoint.State
    STATE_FINISHED: CoopPoint.State
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SELF_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    id: int
    state: CoopPoint.State
    self_confidence: int
    def __init__(self, id: _Optional[int] = ..., state: _Optional[_Union[CoopPoint.State, str]] = ..., self_confidence: _Optional[int] = ...) -> None: ...
