from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CFKEACMDFEL(_message.Message):
    __slots__ = ("BCLMDLDBLGK", "EJNINFFFKJP")
    class BCLMDLDBLGKEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    BCLMDLDBLGK_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    BCLMDLDBLGK: _containers.ScalarMap[int, float]
    EJNINFFFKJP: int
    def __init__(self, BCLMDLDBLGK: _Optional[_Mapping[int, float]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
