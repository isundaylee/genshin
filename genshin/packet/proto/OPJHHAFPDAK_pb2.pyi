from genshin.packet.proto import CNHHCBOMMBH_pb2 as _CNHHCBOMMBH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OPJHHAFPDAK(_message.Message):
    __slots__ = ("EMIPFNGKDPK", "NMIKCMLKNDM", "MPFLDFDOGAI")
    EMIPFNGKDPK_FIELD_NUMBER: _ClassVar[int]
    NMIKCMLKNDM_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    EMIPFNGKDPK: _containers.RepeatedCompositeFieldContainer[_CNHHCBOMMBH_pb2.CNHHCBOMMBH]
    NMIKCMLKNDM: int
    MPFLDFDOGAI: bool
    def __init__(self, EMIPFNGKDPK: _Optional[_Iterable[_Union[_CNHHCBOMMBH_pb2.CNHHCBOMMBH, _Mapping]]] = ..., NMIKCMLKNDM: _Optional[int] = ..., MPFLDFDOGAI: bool = ...) -> None: ...
