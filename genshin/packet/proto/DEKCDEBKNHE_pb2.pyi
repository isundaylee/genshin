from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DEKCDEBKNHE(_message.Message):
    __slots__ = ("GBHBBLGHDLJ", "EJNINFFFKJP")
    class GBHBBLGHDLJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    GBHBBLGHDLJ_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    GBHBBLGHDLJ: _containers.ScalarMap[int, int]
    EJNINFFFKJP: int
    def __init__(self, GBHBBLGHDLJ: _Optional[_Mapping[int, int]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
