from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FABGOAPPDAO(_message.Message):
    __slots__ = ("JAALIDNIKJA", "JFJBENNGKBB", "AFOHHEJBGIB", "JEENPIDKKLM", "FIKLBLMACIB")
    JAALIDNIKJA_FIELD_NUMBER: _ClassVar[int]
    JFJBENNGKBB_FIELD_NUMBER: _ClassVar[int]
    AFOHHEJBGIB_FIELD_NUMBER: _ClassVar[int]
    JEENPIDKKLM_FIELD_NUMBER: _ClassVar[int]
    FIKLBLMACIB_FIELD_NUMBER: _ClassVar[int]
    JAALIDNIKJA: bool
    JFJBENNGKBB: bool
    AFOHHEJBGIB: bool
    JEENPIDKKLM: bool
    FIKLBLMACIB: int
    def __init__(self, JAALIDNIKJA: bool = ..., JFJBENNGKBB: bool = ..., AFOHHEJBGIB: bool = ..., JEENPIDKKLM: bool = ..., FIKLBLMACIB: _Optional[int] = ...) -> None: ...
