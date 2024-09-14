from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeAvatarSummonFinishRsp(_message.Message):
    __slots__ = ("retcode", "event_id")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    event_id: int
    def __init__(self, retcode: _Optional[int] = ..., event_id: _Optional[int] = ...) -> None: ...
