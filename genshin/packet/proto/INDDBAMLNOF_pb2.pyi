from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class INDDBAMLNOF(_message.Message):
    __slots__ = ("HNEMPAAGMDN", "CAKPDNKKGEN", "EJNINFFFKJP")
    HNEMPAAGMDN_FIELD_NUMBER: _ClassVar[int]
    CAKPDNKKGEN_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    HNEMPAAGMDN: _containers.RepeatedScalarFieldContainer[int]
    CAKPDNKKGEN: int
    EJNINFFFKJP: int
    def __init__(self, HNEMPAAGMDN: _Optional[_Iterable[int]] = ..., CAKPDNKKGEN: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
