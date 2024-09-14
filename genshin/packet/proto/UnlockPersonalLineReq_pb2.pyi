from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnlockPersonalLineReq(_message.Message):
    __slots__ = ("personal_line_id",)
    PERSONAL_LINE_ID_FIELD_NUMBER: _ClassVar[int]
    personal_line_id: int
    def __init__(self, personal_line_id: _Optional[int] = ...) -> None: ...
