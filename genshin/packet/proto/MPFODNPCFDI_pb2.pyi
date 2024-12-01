from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MPFODNPCFDI(_message.Message):
    __slots__ = ("str_param", "flt_param", "int_param")
    STR_PARAM_FIELD_NUMBER: _ClassVar[int]
    FLT_PARAM_FIELD_NUMBER: _ClassVar[int]
    INT_PARAM_FIELD_NUMBER: _ClassVar[int]
    str_param: str
    flt_param: float
    int_param: int
    def __init__(self, str_param: _Optional[str] = ..., flt_param: _Optional[float] = ..., int_param: _Optional[int] = ...) -> None: ...
