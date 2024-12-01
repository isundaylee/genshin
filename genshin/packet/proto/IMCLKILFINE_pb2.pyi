from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IMCLKILFINE(_message.Message):
    __slots__ = ("AGHNEJINBFJ", "FHCNHPKKONG", "KKPEPKJACEF", "NMAHOMOGPHC", "type")
    AGHNEJINBFJ_FIELD_NUMBER: _ClassVar[int]
    FHCNHPKKONG_FIELD_NUMBER: _ClassVar[int]
    KKPEPKJACEF_FIELD_NUMBER: _ClassVar[int]
    NMAHOMOGPHC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AGHNEJINBFJ: _containers.RepeatedScalarFieldContainer[float]
    FHCNHPKKONG: _containers.RepeatedScalarFieldContainer[int]
    KKPEPKJACEF: _containers.RepeatedScalarFieldContainer[str]
    NMAHOMOGPHC: int
    type: int
    def __init__(self, AGHNEJINBFJ: _Optional[_Iterable[float]] = ..., FHCNHPKKONG: _Optional[_Iterable[int]] = ..., KKPEPKJACEF: _Optional[_Iterable[str]] = ..., NMAHOMOGPHC: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...
