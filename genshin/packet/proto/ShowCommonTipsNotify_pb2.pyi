from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ShowCommonTipsNotify(_message.Message):
    __slots__ = ("title", "close_time", "content")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CLOSE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    title: str
    close_time: int
    content: str
    def __init__(self, title: _Optional[str] = ..., close_time: _Optional[int] = ..., content: _Optional[str] = ...) -> None: ...
