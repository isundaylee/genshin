from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PropValue(_message.Message):
    __slots__ = ("type", "fval", "ival", "val")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FVAL_FIELD_NUMBER: _ClassVar[int]
    IVAL_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    type: int
    fval: float
    ival: int
    val: int
    def __init__(self, type: _Optional[int] = ..., fval: _Optional[float] = ..., ival: _Optional[int] = ..., val: _Optional[int] = ...) -> None: ...
