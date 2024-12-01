from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PALGOGGHKMG(_message.Message):
    __slots__ = ("PNGLGNLNBNM", "JOFKNLDPGCH")
    class PNGLGNLNBNMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    PNGLGNLNBNM_FIELD_NUMBER: _ClassVar[int]
    JOFKNLDPGCH_FIELD_NUMBER: _ClassVar[int]
    PNGLGNLNBNM: _containers.ScalarMap[int, str]
    JOFKNLDPGCH: int
    def __init__(self, PNGLGNLNBNM: _Optional[_Mapping[int, str]] = ..., JOFKNLDPGCH: _Optional[int] = ...) -> None: ...
