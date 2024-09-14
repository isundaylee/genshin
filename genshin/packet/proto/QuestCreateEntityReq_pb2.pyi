from genshin.packet.proto import CreateEntityInfo_pb2 as _CreateEntityInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestCreateEntityReq(_message.Message):
    __slots__ = ("quest_id", "parent_quest_id", "is_rewind", "entity")
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    IS_REWIND_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    quest_id: int
    parent_quest_id: int
    is_rewind: bool
    entity: _CreateEntityInfo_pb2.CreateEntityInfo
    def __init__(self, quest_id: _Optional[int] = ..., parent_quest_id: _Optional[int] = ..., is_rewind: bool = ..., entity: _Optional[_Union[_CreateEntityInfo_pb2.CreateEntityInfo, _Mapping]] = ...) -> None: ...
