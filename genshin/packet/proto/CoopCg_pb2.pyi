from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CoopCg(_message.Message):
    __slots__ = ("id", "is_unlock")
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_UNLOCK_FIELD_NUMBER: _ClassVar[int]
    id: int
    is_unlock: bool
    def __init__(self, id: _Optional[int] = ..., is_unlock: bool = ...) -> None: ...
