from genshin.packet.proto import ILLBOJCLABL_pb2 as _ILLBOJCLABL_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PCMMBLEAOAJ(_message.Message):
    __slots__ = ("BODIEJCLGMB", "OACIPABKFNP", "OAJOOBGHAGM")
    BODIEJCLGMB_FIELD_NUMBER: _ClassVar[int]
    OACIPABKFNP_FIELD_NUMBER: _ClassVar[int]
    OAJOOBGHAGM_FIELD_NUMBER: _ClassVar[int]
    BODIEJCLGMB: _ILLBOJCLABL_pb2.ILLBOJCLABL
    OACIPABKFNP: int
    OAJOOBGHAGM: int
    def __init__(self, BODIEJCLGMB: _Optional[_Union[_ILLBOJCLABL_pb2.ILLBOJCLABL, str]] = ..., OACIPABKFNP: _Optional[int] = ..., OAJOOBGHAGM: _Optional[int] = ...) -> None: ...
