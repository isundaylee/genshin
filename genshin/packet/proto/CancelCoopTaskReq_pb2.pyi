from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CancelCoopTaskReq(_message.Message):
    __slots__ = ("chapter_id",)
    CHAPTER_ID_FIELD_NUMBER: _ClassVar[int]
    chapter_id: int
    def __init__(self, chapter_id: _Optional[int] = ...) -> None: ...
