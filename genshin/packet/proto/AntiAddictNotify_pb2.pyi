from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AntiAddictNotify(_message.Message):
    __slots__ = ("level", "msg_type", "msg")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    level: str
    msg_type: int
    msg: str
    def __init__(self, level: _Optional[str] = ..., msg_type: _Optional[int] = ..., msg: _Optional[str] = ...) -> None: ...
