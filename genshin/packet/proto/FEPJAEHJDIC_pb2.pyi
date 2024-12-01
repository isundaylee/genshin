from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FEPJAEHJDIC(_message.Message):
    __slots__ = ("MDFMDEHCDFP", "GICJOFMFPIB", "KBDNNJFODDG", "FNAHIHOCNOC")
    class KBDNNJFODDGEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MDFMDEHCDFP_FIELD_NUMBER: _ClassVar[int]
    GICJOFMFPIB_FIELD_NUMBER: _ClassVar[int]
    KBDNNJFODDG_FIELD_NUMBER: _ClassVar[int]
    FNAHIHOCNOC_FIELD_NUMBER: _ClassVar[int]
    MDFMDEHCDFP: _containers.RepeatedScalarFieldContainer[int]
    GICJOFMFPIB: _containers.RepeatedScalarFieldContainer[int]
    KBDNNJFODDG: _containers.ScalarMap[int, int]
    FNAHIHOCNOC: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, MDFMDEHCDFP: _Optional[_Iterable[int]] = ..., GICJOFMFPIB: _Optional[_Iterable[int]] = ..., KBDNNJFODDG: _Optional[_Mapping[int, int]] = ..., FNAHIHOCNOC: _Optional[_Iterable[int]] = ...) -> None: ...
