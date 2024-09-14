from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetBattlePassViewedReq(_message.Message):
    __slots__ = ("schedule_id",)
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    schedule_id: int
    def __init__(self, schedule_id: _Optional[int] = ...) -> None: ...
