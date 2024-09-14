from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddQuestContentProgressRsp(_message.Message):
    __slots__ = ("content_type", "retcode")
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    content_type: int
    retcode: int
    def __init__(self, content_type: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
