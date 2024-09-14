from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvestigationTarget(_message.Message):
    __slots__ = ("progress", "total_progress", "investigation_id", "quest_id", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID: _ClassVar[InvestigationTarget.State]
        IN_PROGRESS: _ClassVar[InvestigationTarget.State]
        COMPLETE: _ClassVar[InvestigationTarget.State]
        REWARD_TAKEN: _ClassVar[InvestigationTarget.State]
    INVALID: InvestigationTarget.State
    IN_PROGRESS: InvestigationTarget.State
    COMPLETE: InvestigationTarget.State
    REWARD_TAKEN: InvestigationTarget.State
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    INVESTIGATION_ID_FIELD_NUMBER: _ClassVar[int]
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    progress: int
    total_progress: int
    investigation_id: int
    quest_id: int
    state: InvestigationTarget.State
    def __init__(self, progress: _Optional[int] = ..., total_progress: _Optional[int] = ..., investigation_id: _Optional[int] = ..., quest_id: _Optional[int] = ..., state: _Optional[_Union[InvestigationTarget.State, str]] = ...) -> None: ...
