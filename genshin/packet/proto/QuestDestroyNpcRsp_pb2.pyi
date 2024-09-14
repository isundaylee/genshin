from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuestDestroyNpcRsp(_message.Message):
    __slots__ = ("parent_quest_id", "retcode", "npc_id")
    PARENT_QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    NPC_ID_FIELD_NUMBER: _ClassVar[int]
    parent_quest_id: int
    retcode: int
    npc_id: int
    def __init__(self, parent_quest_id: _Optional[int] = ..., retcode: _Optional[int] = ..., npc_id: _Optional[int] = ...) -> None: ...
