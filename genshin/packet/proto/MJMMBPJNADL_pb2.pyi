from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MJMMBPJNADL(_message.Message):
    __slots__ = ("EFANDLIBEJL", "HJJHGLIKCAM", "EHHBAAEJFGL")
    class EFANDLIBEJLEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    EFANDLIBEJL_FIELD_NUMBER: _ClassVar[int]
    HJJHGLIKCAM_FIELD_NUMBER: _ClassVar[int]
    EHHBAAEJFGL_FIELD_NUMBER: _ClassVar[int]
    EFANDLIBEJL: _containers.ScalarMap[int, int]
    HJJHGLIKCAM: int
    EHHBAAEJFGL: int
    def __init__(self, EFANDLIBEJL: _Optional[_Mapping[int, int]] = ..., HJJHGLIKCAM: _Optional[int] = ..., EHHBAAEJFGL: _Optional[int] = ...) -> None: ...
