from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuestVarOp(_message.Message):
    __slots__ = ("index", "is_add", "value")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_ADD_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    index: int
    is_add: bool
    value: int
    def __init__(self, index: _Optional[int] = ..., is_add: bool = ..., value: _Optional[int] = ...) -> None: ...
