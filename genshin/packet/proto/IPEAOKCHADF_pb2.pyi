from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IPEAOKCHADF(_message.Message):
    __slots__ = ("NCCPPHNNPBF", "NJPJCGCNEDO", "CPIBLKPDDDN")
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    NJPJCGCNEDO_FIELD_NUMBER: _ClassVar[int]
    CPIBLKPDDDN_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF: int
    NJPJCGCNEDO: int
    CPIBLKPDDDN: bool
    def __init__(self, NCCPPHNNPBF: _Optional[int] = ..., NJPJCGCNEDO: _Optional[int] = ..., CPIBLKPDDDN: bool = ...) -> None: ...
