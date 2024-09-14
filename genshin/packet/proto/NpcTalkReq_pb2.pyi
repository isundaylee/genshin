from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NpcTalkReq(_message.Message):
    __slots__ = ("entity_id", "talk_id", "npc_entity_id")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TALK_ID_FIELD_NUMBER: _ClassVar[int]
    NPC_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    talk_id: int
    npc_entity_id: int
    def __init__(self, entity_id: _Optional[int] = ..., talk_id: _Optional[int] = ..., npc_entity_id: _Optional[int] = ...) -> None: ...
