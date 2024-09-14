from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeBlockDotPattern(_message.Message):
    __slots__ = ("height", "data", "width")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    height: int
    data: bytes
    width: int
    def __init__(self, height: _Optional[int] = ..., data: _Optional[bytes] = ..., width: _Optional[int] = ...) -> None: ...
