from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TakeInvestigationTargetRewardReq(_message.Message):
    __slots__ = ("quest_id",)
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    quest_id: int
    def __init__(self, quest_id: _Optional[int] = ...) -> None: ...
