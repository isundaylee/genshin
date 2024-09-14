from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NpcTalkRsp(_message.Message):
    __slots__ = ("retcode", "npc_entity_id", "cur_talk_id", "entity_id")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    NPC_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CUR_TALK_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    npc_entity_id: int
    cur_talk_id: int
    entity_id: int
    def __init__(self, retcode: _Optional[int] = ..., npc_entity_id: _Optional[int] = ..., cur_talk_id: _Optional[int] = ..., entity_id: _Optional[int] = ...) -> None: ...
