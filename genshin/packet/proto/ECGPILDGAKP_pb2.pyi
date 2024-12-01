from genshin.packet.proto import FGNHPFIDPCB_pb2 as _FGNHPFIDPCB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ECGPILDGAKP(_message.Message):
    __slots__ = ("CHHGPNNNNLP", "OHMKBGAMEIM", "MPPCKLOHOAD", "OCJEEEEFPJM", "CEJKBIKGFBO", "LKNPJAHAILB", "AEGNLDMDKJL", "NIMMILCCDOO")
    CHHGPNNNNLP_FIELD_NUMBER: _ClassVar[int]
    OHMKBGAMEIM_FIELD_NUMBER: _ClassVar[int]
    MPPCKLOHOAD_FIELD_NUMBER: _ClassVar[int]
    OCJEEEEFPJM_FIELD_NUMBER: _ClassVar[int]
    CEJKBIKGFBO_FIELD_NUMBER: _ClassVar[int]
    LKNPJAHAILB_FIELD_NUMBER: _ClassVar[int]
    AEGNLDMDKJL_FIELD_NUMBER: _ClassVar[int]
    NIMMILCCDOO_FIELD_NUMBER: _ClassVar[int]
    CHHGPNNNNLP: _FGNHPFIDPCB_pb2.FGNHPFIDPCB
    OHMKBGAMEIM: _containers.RepeatedScalarFieldContainer[str]
    MPPCKLOHOAD: str
    OCJEEEEFPJM: int
    CEJKBIKGFBO: int
    LKNPJAHAILB: int
    AEGNLDMDKJL: int
    NIMMILCCDOO: int
    def __init__(self, CHHGPNNNNLP: _Optional[_Union[_FGNHPFIDPCB_pb2.FGNHPFIDPCB, _Mapping]] = ..., OHMKBGAMEIM: _Optional[_Iterable[str]] = ..., MPPCKLOHOAD: _Optional[str] = ..., OCJEEEEFPJM: _Optional[int] = ..., CEJKBIKGFBO: _Optional[int] = ..., LKNPJAHAILB: _Optional[int] = ..., AEGNLDMDKJL: _Optional[int] = ..., NIMMILCCDOO: _Optional[int] = ...) -> None: ...
