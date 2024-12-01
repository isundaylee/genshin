from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ACEKDEBFIMC(_message.Message):
    __slots__ = ("EIFAILJDGDG", "JBLNJPIGCGE")
    class JBLNJPIGCGEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    EIFAILJDGDG_FIELD_NUMBER: _ClassVar[int]
    JBLNJPIGCGE_FIELD_NUMBER: _ClassVar[int]
    EIFAILJDGDG: _containers.RepeatedScalarFieldContainer[int]
    JBLNJPIGCGE: _containers.ScalarMap[int, int]
    def __init__(self, EIFAILJDGDG: _Optional[_Iterable[int]] = ..., JBLNJPIGCGE: _Optional[_Mapping[int, int]] = ...) -> None: ...
