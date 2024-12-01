from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DPFDNAEFABC(_message.Message):
    __slots__ = ("is_locked", "NDCDMPINDOI")
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    NDCDMPINDOI_FIELD_NUMBER: _ClassVar[int]
    is_locked: bool
    NDCDMPINDOI: int
    def __init__(self, is_locked: bool = ..., NDCDMPINDOI: _Optional[int] = ...) -> None: ...
