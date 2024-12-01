from genshin.packet.proto import FGNHPFIDPCB_pb2 as _FGNHPFIDPCB_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JAFNAFFNFLD(_message.Message):
    __slots__ = ("DDKFGHONPDC", "MDMMNLEEMDF")
    DDKFGHONPDC_FIELD_NUMBER: _ClassVar[int]
    MDMMNLEEMDF_FIELD_NUMBER: _ClassVar[int]
    DDKFGHONPDC: _FGNHPFIDPCB_pb2.FGNHPFIDPCB
    MDMMNLEEMDF: float
    def __init__(self, DDKFGHONPDC: _Optional[_Union[_FGNHPFIDPCB_pb2.FGNHPFIDPCB, _Mapping]] = ..., MDMMNLEEMDF: _Optional[float] = ...) -> None: ...
