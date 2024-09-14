from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SceneNpcInfo(_message.Message):
    __slots__ = ("npc_id", "room_id", "parent_quest_id", "block_id")
    NPC_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    npc_id: int
    room_id: int
    parent_quest_id: int
    block_id: int
    def __init__(self, npc_id: _Optional[int] = ..., room_id: _Optional[int] = ..., parent_quest_id: _Optional[int] = ..., block_id: _Optional[int] = ...) -> None: ...
