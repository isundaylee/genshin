from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BreakoutElementReactionCounter(_message.Message):
    __slots__ = ("element_reaction", "count")
    ELEMENT_REACTION_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    element_reaction: int
    count: int
    def __init__(self, element_reaction: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
