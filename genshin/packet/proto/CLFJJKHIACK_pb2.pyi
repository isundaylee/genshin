from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CLFJJKHIACK(_message.Message):
    __slots__ = ("PCAFMBNPEBM", "EPFCIDIKLKG", "KCFDPKKBECP", "FPGEOPBMAJH")
    class PCAFMBNPEBMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PCAFMBNPEBM_FIELD_NUMBER: _ClassVar[int]
    EPFCIDIKLKG_FIELD_NUMBER: _ClassVar[int]
    KCFDPKKBECP_FIELD_NUMBER: _ClassVar[int]
    FPGEOPBMAJH_FIELD_NUMBER: _ClassVar[int]
    PCAFMBNPEBM: _containers.ScalarMap[int, int]
    EPFCIDIKLKG: int
    KCFDPKKBECP: bool
    FPGEOPBMAJH: bool
    def __init__(self, PCAFMBNPEBM: _Optional[_Mapping[int, int]] = ..., EPFCIDIKLKG: _Optional[int] = ..., KCFDPKKBECP: bool = ..., FPGEOPBMAJH: bool = ...) -> None: ...
