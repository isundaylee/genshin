from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuestUpdateQuestVarNotify(_message.Message):
    __slots__ = ("parent_quest_id", "parent_quest_var_seq", "quest_var")
    PARENT_QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_QUEST_VAR_SEQ_FIELD_NUMBER: _ClassVar[int]
    QUEST_VAR_FIELD_NUMBER: _ClassVar[int]
    parent_quest_id: int
    parent_quest_var_seq: int
    quest_var: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, parent_quest_id: _Optional[int] = ..., parent_quest_var_seq: _Optional[int] = ..., quest_var: _Optional[_Iterable[int]] = ...) -> None: ...
