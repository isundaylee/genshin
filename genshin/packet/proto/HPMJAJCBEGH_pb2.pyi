from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HPMJAJCBEGH(_message.Message):
    __slots__ = ("NJFHJGJILCK", "EJCGAAPOGGN", "NCCPPHNNPBF")
    class NJFHJGJILCKEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class EJCGAAPOGGNEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NJFHJGJILCK_FIELD_NUMBER: _ClassVar[int]
    EJCGAAPOGGN_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    NJFHJGJILCK: _containers.ScalarMap[int, int]
    EJCGAAPOGGN: _containers.ScalarMap[int, int]
    NCCPPHNNPBF: int
    def __init__(self, NJFHJGJILCK: _Optional[_Mapping[int, int]] = ..., EJCGAAPOGGN: _Optional[_Mapping[int, int]] = ..., NCCPPHNNPBF: _Optional[int] = ...) -> None: ...
