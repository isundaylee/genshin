from genshin.packet.proto import FGNHPFIDPCB_pb2 as _FGNHPFIDPCB_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OLNKDKCNLAM(_message.Message):
    __slots__ = ("MJNIEHCAKGA", "CHHGPNNNNLP", "HBJEGBKEFIP", "LKNPJAHAILB")
    MJNIEHCAKGA_FIELD_NUMBER: _ClassVar[int]
    CHHGPNNNNLP_FIELD_NUMBER: _ClassVar[int]
    HBJEGBKEFIP_FIELD_NUMBER: _ClassVar[int]
    LKNPJAHAILB_FIELD_NUMBER: _ClassVar[int]
    MJNIEHCAKGA: _FGNHPFIDPCB_pb2.FGNHPFIDPCB
    CHHGPNNNNLP: _FGNHPFIDPCB_pb2.FGNHPFIDPCB
    HBJEGBKEFIP: int
    LKNPJAHAILB: int
    def __init__(self, MJNIEHCAKGA: _Optional[_Union[_FGNHPFIDPCB_pb2.FGNHPFIDPCB, _Mapping]] = ..., CHHGPNNNNLP: _Optional[_Union[_FGNHPFIDPCB_pb2.FGNHPFIDPCB, _Mapping]] = ..., HBJEGBKEFIP: _Optional[int] = ..., LKNPJAHAILB: _Optional[int] = ...) -> None: ...
