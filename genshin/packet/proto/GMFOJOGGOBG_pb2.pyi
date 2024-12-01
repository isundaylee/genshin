from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GMFOJOGGOBG(_message.Message):
    __slots__ = ("CGGJDKLLGLE", "AGJOJGPDNAL", "NCCPPHNNPBF")
    class CGGJDKLLGLEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class AGJOJGPDNALEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    CGGJDKLLGLE_FIELD_NUMBER: _ClassVar[int]
    AGJOJGPDNAL_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    CGGJDKLLGLE: _containers.ScalarMap[int, int]
    AGJOJGPDNAL: _containers.ScalarMap[int, int]
    NCCPPHNNPBF: int
    def __init__(self, CGGJDKLLGLE: _Optional[_Mapping[int, int]] = ..., AGJOJGPDNAL: _Optional[_Mapping[int, int]] = ..., NCCPPHNNPBF: _Optional[int] = ...) -> None: ...
