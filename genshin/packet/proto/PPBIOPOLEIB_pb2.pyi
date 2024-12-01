from genshin.packet.proto import BBICGHBHCBA_pb2 as _BBICGHBHCBA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PPBIOPOLEIB(_message.Message):
    __slots__ = ("LABBIMKCLJE", "JFLLLBICCIH", "IEJPGHNLIDB", "GLKNGDDNOCN", "MPNJAOCKMAH", "DJAIIDLDAJM")
    LABBIMKCLJE_FIELD_NUMBER: _ClassVar[int]
    JFLLLBICCIH_FIELD_NUMBER: _ClassVar[int]
    IEJPGHNLIDB_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    DJAIIDLDAJM_FIELD_NUMBER: _ClassVar[int]
    LABBIMKCLJE: _BBICGHBHCBA_pb2.BBICGHBHCBA
    JFLLLBICCIH: _containers.RepeatedCompositeFieldContainer[_BBICGHBHCBA_pb2.BBICGHBHCBA]
    IEJPGHNLIDB: int
    GLKNGDDNOCN: bool
    MPNJAOCKMAH: int
    DJAIIDLDAJM: int
    def __init__(self, LABBIMKCLJE: _Optional[_Union[_BBICGHBHCBA_pb2.BBICGHBHCBA, _Mapping]] = ..., JFLLLBICCIH: _Optional[_Iterable[_Union[_BBICGHBHCBA_pb2.BBICGHBHCBA, _Mapping]]] = ..., IEJPGHNLIDB: _Optional[int] = ..., GLKNGDDNOCN: bool = ..., MPNJAOCKMAH: _Optional[int] = ..., DJAIIDLDAJM: _Optional[int] = ...) -> None: ...
