from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KAPNLPKPHPD(_message.Message):
    __slots__ = ("BMANEJIIMAH", "DDHIPEJAMBC")
    class BMANEJIIMAHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BMANEJIIMAH_FIELD_NUMBER: _ClassVar[int]
    DDHIPEJAMBC_FIELD_NUMBER: _ClassVar[int]
    BMANEJIIMAH: _containers.ScalarMap[int, int]
    DDHIPEJAMBC: bool
    def __init__(self, BMANEJIIMAH: _Optional[_Mapping[int, int]] = ..., DDHIPEJAMBC: bool = ...) -> None: ...
