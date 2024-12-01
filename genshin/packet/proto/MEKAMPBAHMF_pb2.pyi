from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MEKAMPBAHMF(_message.Message):
    __slots__ = ("KEGIGLEINKL", "JNNLEBGECDL", "EJNINFFFKJP")
    class JNNLEBGECDLEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    KEGIGLEINKL_FIELD_NUMBER: _ClassVar[int]
    JNNLEBGECDL_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    KEGIGLEINKL: _containers.RepeatedScalarFieldContainer[int]
    JNNLEBGECDL: _containers.ScalarMap[int, int]
    EJNINFFFKJP: int
    def __init__(self, KEGIGLEINKL: _Optional[_Iterable[int]] = ..., JNNLEBGECDL: _Optional[_Mapping[int, int]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
