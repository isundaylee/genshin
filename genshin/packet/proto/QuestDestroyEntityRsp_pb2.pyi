from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuestDestroyEntityRsp(_message.Message):
    __slots__ = ("entity_id", "quest_id", "retcode", "scene_id")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    quest_id: int
    retcode: int
    scene_id: int
    def __init__(self, entity_id: _Optional[int] = ..., quest_id: _Optional[int] = ..., retcode: _Optional[int] = ..., scene_id: _Optional[int] = ...) -> None: ...
