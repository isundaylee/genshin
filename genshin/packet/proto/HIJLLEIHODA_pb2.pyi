from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HIJLLEIHODA(_message.Message):
    __slots__ = ("LCGABJIJCBF", "CDIJINMEJLJ", "GLKNGDDNOCN", "IDIBOBEFKJA")
    class LCGABJIJCBFEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    LCGABJIJCBF_FIELD_NUMBER: _ClassVar[int]
    CDIJINMEJLJ_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    IDIBOBEFKJA_FIELD_NUMBER: _ClassVar[int]
    LCGABJIJCBF: _containers.ScalarMap[int, int]
    CDIJINMEJLJ: int
    GLKNGDDNOCN: bool
    IDIBOBEFKJA: int
    def __init__(self, LCGABJIJCBF: _Optional[_Mapping[int, int]] = ..., CDIJINMEJLJ: _Optional[int] = ..., GLKNGDDNOCN: bool = ..., IDIBOBEFKJA: _Optional[int] = ...) -> None: ...
