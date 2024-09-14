from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BreakoutBrickInfo(_message.Message):
    __slots__ = ("hp", "element_type")
    HP_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    hp: int
    element_type: int
    def __init__(self, hp: _Optional[int] = ..., element_type: _Optional[int] = ...) -> None: ...
