from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEnterPosInfo(_message.Message):
    __slots__ = ("quest_id", "point_id")
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    POINT_ID_FIELD_NUMBER: _ClassVar[int]
    quest_id: int
    point_id: int
    def __init__(self, quest_id: _Optional[int] = ..., point_id: _Optional[int] = ...) -> None: ...
