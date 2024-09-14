from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionCmd(_message.Message):
    __slots__ = ("message_id", "body")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    body: bytes
    def __init__(self, message_id: _Optional[int] = ..., body: _Optional[bytes] = ...) -> None: ...
