from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BODFNFIDFOD(_message.Message):
    __slots__ = ("JCCGOBKGOJA", "GILNLCACKFO", "ABGMLEMGIOG")
    class JCCGOBKGOJAEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    JCCGOBKGOJA_FIELD_NUMBER: _ClassVar[int]
    GILNLCACKFO_FIELD_NUMBER: _ClassVar[int]
    ABGMLEMGIOG_FIELD_NUMBER: _ClassVar[int]
    JCCGOBKGOJA: _containers.ScalarMap[int, int]
    GILNLCACKFO: int
    ABGMLEMGIOG: int
    def __init__(self, JCCGOBKGOJA: _Optional[_Mapping[int, int]] = ..., GILNLCACKFO: _Optional[int] = ..., ABGMLEMGIOG: _Optional[int] = ...) -> None: ...
