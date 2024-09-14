from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CombineFormulaDataNotify(_message.Message):
    __slots__ = ("combine_id", "is_locked")
    COMBINE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    combine_id: int
    is_locked: bool
    def __init__(self, combine_id: _Optional[int] = ..., is_locked: bool = ...) -> None: ...
