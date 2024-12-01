from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OACPNINELPM(_message.Message):
    __slots__ = ("BMFKOONMMEE", "EJNINFFFKJP", "IHKKICKGNHB", "NCCPPHNNPBF")
    BMFKOONMMEE_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    IHKKICKGNHB_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    BMFKOONMMEE: str
    EJNINFFFKJP: int
    IHKKICKGNHB: bool
    NCCPPHNNPBF: int
    def __init__(self, BMFKOONMMEE: _Optional[str] = ..., EJNINFFFKJP: _Optional[int] = ..., IHKKICKGNHB: bool = ..., NCCPPHNNPBF: _Optional[int] = ...) -> None: ...
