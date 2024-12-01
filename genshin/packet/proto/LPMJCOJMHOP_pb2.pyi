from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LPMJCOJMHOP(_message.Message):
    __slots__ = ("GDJOMHLOEOH", "GAINCCNCANO")
    class GDJOMHLOEOHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    GDJOMHLOEOH_FIELD_NUMBER: _ClassVar[int]
    GAINCCNCANO_FIELD_NUMBER: _ClassVar[int]
    GDJOMHLOEOH: _containers.ScalarMap[int, int]
    GAINCCNCANO: int
    def __init__(self, GDJOMHLOEOH: _Optional[_Mapping[int, int]] = ..., GAINCCNCANO: _Optional[int] = ...) -> None: ...
