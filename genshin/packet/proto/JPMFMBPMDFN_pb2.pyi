from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class JPMFMBPMDFN(_message.Message):
    __slots__ = ("OCMCGGCJLBB", "FJCNNENEKBM")
    OCMCGGCJLBB_FIELD_NUMBER: _ClassVar[int]
    FJCNNENEKBM_FIELD_NUMBER: _ClassVar[int]
    OCMCGGCJLBB: _containers.RepeatedScalarFieldContainer[int]
    FJCNNENEKBM: int
    def __init__(self, OCMCGGCJLBB: _Optional[_Iterable[int]] = ..., FJCNNENEKBM: _Optional[int] = ...) -> None: ...
