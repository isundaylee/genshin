from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeAvatarSummonEventRsp(_message.Message):
    __slots__ = ("event_id", "retcode")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    retcode: int
    def __init__(self, event_id: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
