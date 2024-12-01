from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KCBMFCPADFO(_message.Message):
    __slots__ = ("IBGBHIMFGOL", "GBEEEDLGPOB")
    class GBEEEDLGPOBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    IBGBHIMFGOL_FIELD_NUMBER: _ClassVar[int]
    GBEEEDLGPOB_FIELD_NUMBER: _ClassVar[int]
    IBGBHIMFGOL: _containers.RepeatedScalarFieldContainer[int]
    GBEEEDLGPOB: _containers.ScalarMap[int, int]
    def __init__(self, IBGBHIMFGOL: _Optional[_Iterable[int]] = ..., GBEEEDLGPOB: _Optional[_Mapping[int, int]] = ...) -> None: ...
