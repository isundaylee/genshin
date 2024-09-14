from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddQuestContentProgressReq(_message.Message):
    __slots__ = ("content_type", "param", "add_progress")
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    ADD_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    content_type: int
    param: int
    add_progress: int
    def __init__(self, content_type: _Optional[int] = ..., param: _Optional[int] = ..., add_progress: _Optional[int] = ...) -> None: ...
