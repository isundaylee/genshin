from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PEEBELMDIEC(_message.Message):
    __slots__ = ("MLIFPDABPCF", "HOCBHPDHPLF", "LHAMFACKEMF", "EIKKFELNGIJ")
    MLIFPDABPCF_FIELD_NUMBER: _ClassVar[int]
    HOCBHPDHPLF_FIELD_NUMBER: _ClassVar[int]
    LHAMFACKEMF_FIELD_NUMBER: _ClassVar[int]
    EIKKFELNGIJ_FIELD_NUMBER: _ClassVar[int]
    MLIFPDABPCF: bool
    HOCBHPDHPLF: bool
    LHAMFACKEMF: bool
    EIKKFELNGIJ: int
    def __init__(self, MLIFPDABPCF: bool = ..., HOCBHPDHPLF: bool = ..., LHAMFACKEMF: bool = ..., EIKKFELNGIJ: _Optional[int] = ...) -> None: ...
