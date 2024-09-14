from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AnimatorParameterValueInfo(_message.Message):
    __slots__ = ("para_type", "int_val", "float_val", "bool_val")
    PARA_TYPE_FIELD_NUMBER: _ClassVar[int]
    INT_VAL_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VAL_FIELD_NUMBER: _ClassVar[int]
    BOOL_VAL_FIELD_NUMBER: _ClassVar[int]
    para_type: int
    int_val: int
    float_val: float
    bool_val: bool
    def __init__(self, para_type: _Optional[int] = ..., int_val: _Optional[int] = ..., float_val: _Optional[float] = ..., bool_val: bool = ...) -> None: ...
