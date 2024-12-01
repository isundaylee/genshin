from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FGNHPFIDPCB(_message.Message):
    __slots__ = ("str", "hash")
    STR_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    str: str
    hash: int
    def __init__(self, str: _Optional[str] = ..., hash: _Optional[int] = ...) -> None: ...
