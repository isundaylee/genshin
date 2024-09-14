from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StopServerInfo(_message.Message):
    __slots__ = ("stop_begin_time", "stop_end_time", "url", "content_msg")
    STOP_BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    STOP_END_TIME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MSG_FIELD_NUMBER: _ClassVar[int]
    stop_begin_time: int
    stop_end_time: int
    url: str
    content_msg: str
    def __init__(self, stop_begin_time: _Optional[int] = ..., stop_end_time: _Optional[int] = ..., url: _Optional[str] = ..., content_msg: _Optional[str] = ...) -> None: ...
