from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuestTransmitRsp(_message.Message):
    __slots__ = ("quest_id", "point_id", "retcode")
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    POINT_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    quest_id: int
    point_id: int
    retcode: int
    def __init__(self, quest_id: _Optional[int] = ..., point_id: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
