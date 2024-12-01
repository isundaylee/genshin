from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LJAPPOBJNEH(_message.Message):
    __slots__ = ("IJLFKCCOONM", "NCCPPHNNPBF", "DNBEFLJLAMB")
    class IJLFKCCOONMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    IJLFKCCOONM_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    IJLFKCCOONM: _containers.ScalarMap[int, int]
    NCCPPHNNPBF: int
    DNBEFLJLAMB: int
    def __init__(self, IJLFKCCOONM: _Optional[_Mapping[int, int]] = ..., NCCPPHNNPBF: _Optional[int] = ..., DNBEFLJLAMB: _Optional[int] = ...) -> None: ...
