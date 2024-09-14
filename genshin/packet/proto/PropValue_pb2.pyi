from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PropValue(_message.Message):
    __slots__ = ("type", "val", "ival", "fval")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    IVAL_FIELD_NUMBER: _ClassVar[int]
    FVAL_FIELD_NUMBER: _ClassVar[int]
    type: int
    val: int
    ival: int
    fval: float
    def __init__(self, type: _Optional[int] = ..., val: _Optional[int] = ..., ival: _Optional[int] = ..., fval: _Optional[float] = ...) -> None: ...
