from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BOCHGCPIBPI(_message.Message):
    __slots__ = ("IJLFKCCOONM", "DNBEFLJLAMB", "EJNINFFFKJP")
    class IJLFKCCOONMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    IJLFKCCOONM_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    IJLFKCCOONM: _containers.ScalarMap[int, int]
    DNBEFLJLAMB: int
    EJNINFFFKJP: int
    def __init__(self, IJLFKCCOONM: _Optional[_Mapping[int, int]] = ..., DNBEFLJLAMB: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
