from genshin.packet.proto import HIPGPMNCMBP_pb2 as _HIPGPMNCMBP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OCAAMCABKGG(_message.Message):
    __slots__ = ("EEKFELFANGN", "FGOLICDLFKG", "ENBNEMMEFBN", "LKOFKODPMGO", "FHAIHPBKOBI")
    EEKFELFANGN_FIELD_NUMBER: _ClassVar[int]
    FGOLICDLFKG_FIELD_NUMBER: _ClassVar[int]
    ENBNEMMEFBN_FIELD_NUMBER: _ClassVar[int]
    LKOFKODPMGO_FIELD_NUMBER: _ClassVar[int]
    FHAIHPBKOBI_FIELD_NUMBER: _ClassVar[int]
    EEKFELFANGN: _containers.RepeatedScalarFieldContainer[int]
    FGOLICDLFKG: int
    ENBNEMMEFBN: _HIPGPMNCMBP_pb2.HIPGPMNCMBP
    LKOFKODPMGO: int
    FHAIHPBKOBI: int
    def __init__(self, EEKFELFANGN: _Optional[_Iterable[int]] = ..., FGOLICDLFKG: _Optional[int] = ..., ENBNEMMEFBN: _Optional[_Union[_HIPGPMNCMBP_pb2.HIPGPMNCMBP, str]] = ..., LKOFKODPMGO: _Optional[int] = ..., FHAIHPBKOBI: _Optional[int] = ...) -> None: ...
