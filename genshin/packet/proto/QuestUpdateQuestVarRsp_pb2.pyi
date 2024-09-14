from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuestUpdateQuestVarRsp(_message.Message):
    __slots__ = ("parent_quest_var_seq", "parent_quest_id", "quest_id", "retcode")
    PARENT_QUEST_VAR_SEQ_FIELD_NUMBER: _ClassVar[int]
    PARENT_QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    parent_quest_var_seq: int
    parent_quest_id: int
    quest_id: int
    retcode: int
    def __init__(self, parent_quest_var_seq: _Optional[int] = ..., parent_quest_id: _Optional[int] = ..., quest_id: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
