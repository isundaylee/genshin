from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DGOLKHNIHBM(_message.Message):
    __slots__ = ("LHNAAHBGEHE", "LKOFKODPMGO")
    class LHNAAHBGEHEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    LHNAAHBGEHE_FIELD_NUMBER: _ClassVar[int]
    LKOFKODPMGO_FIELD_NUMBER: _ClassVar[int]
    LHNAAHBGEHE: _containers.ScalarMap[int, int]
    LKOFKODPMGO: int
    def __init__(self, LHNAAHBGEHE: _Optional[_Mapping[int, int]] = ..., LKOFKODPMGO: _Optional[int] = ...) -> None: ...
