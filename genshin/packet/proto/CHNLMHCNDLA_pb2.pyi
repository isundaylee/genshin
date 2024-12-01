from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CHNLMHCNDLA(_message.Message):
    __slots__ = ("CIAGBMAMDNJ", "JNHDKJDBICL")
    class CIAGBMAMDNJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    CIAGBMAMDNJ_FIELD_NUMBER: _ClassVar[int]
    JNHDKJDBICL_FIELD_NUMBER: _ClassVar[int]
    CIAGBMAMDNJ: _containers.ScalarMap[int, int]
    JNHDKJDBICL: int
    def __init__(self, CIAGBMAMDNJ: _Optional[_Mapping[int, int]] = ..., JNHDKJDBICL: _Optional[int] = ...) -> None: ...
