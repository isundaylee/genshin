from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MailTextContent(_message.Message):
    __slots__ = ("title", "content", "sender")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    title: str
    content: str
    sender: str
    def __init__(self, title: _Optional[str] = ..., content: _Optional[str] = ..., sender: _Optional[str] = ...) -> None: ...
