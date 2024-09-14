from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuestDestroyEntityReq(_message.Message):
    __slots__ = ("quest_id", "entity_id", "scene_id")
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    quest_id: int
    entity_id: int
    scene_id: int
    def __init__(self, quest_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., scene_id: _Optional[int] = ...) -> None: ...
