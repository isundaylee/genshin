from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AHMBOOGJKDJ(_message.Message):
    __slots__ = ("LEMCPFECPMB", "JNOFEOHIMOB", "ALKGNKPNKIJ", "MBBKAENBCKD", "KACHBHBOGOL")
    class LEMCPFECPMBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class JNOFEOHIMOBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    LEMCPFECPMB_FIELD_NUMBER: _ClassVar[int]
    JNOFEOHIMOB_FIELD_NUMBER: _ClassVar[int]
    ALKGNKPNKIJ_FIELD_NUMBER: _ClassVar[int]
    MBBKAENBCKD_FIELD_NUMBER: _ClassVar[int]
    KACHBHBOGOL_FIELD_NUMBER: _ClassVar[int]
    LEMCPFECPMB: _containers.ScalarMap[int, int]
    JNOFEOHIMOB: _containers.ScalarMap[int, int]
    ALKGNKPNKIJ: int
    MBBKAENBCKD: int
    KACHBHBOGOL: int
    def __init__(self, LEMCPFECPMB: _Optional[_Mapping[int, int]] = ..., JNOFEOHIMOB: _Optional[_Mapping[int, int]] = ..., ALKGNKPNKIJ: _Optional[int] = ..., MBBKAENBCKD: _Optional[int] = ..., KACHBHBOGOL: _Optional[int] = ...) -> None: ...
