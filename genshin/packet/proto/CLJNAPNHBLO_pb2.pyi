from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CLJNAPNHBLO(_message.Message):
    __slots__ = ("FOOHNBBIHNB", "BKBNBIPFBCF", "IEJPGHNLIDB", "BDCBLNLCAGE", "GLKNGDDNOCN", "IGBDOEBPPHO", "OBCLCJEJIML", "MPNJAOCKMAH")
    FOOHNBBIHNB_FIELD_NUMBER: _ClassVar[int]
    BKBNBIPFBCF_FIELD_NUMBER: _ClassVar[int]
    IEJPGHNLIDB_FIELD_NUMBER: _ClassVar[int]
    BDCBLNLCAGE_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    OBCLCJEJIML_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    FOOHNBBIHNB: _containers.RepeatedScalarFieldContainer[int]
    BKBNBIPFBCF: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    IEJPGHNLIDB: int
    BDCBLNLCAGE: bool
    GLKNGDDNOCN: bool
    IGBDOEBPPHO: int
    OBCLCJEJIML: float
    MPNJAOCKMAH: int
    def __init__(self, FOOHNBBIHNB: _Optional[_Iterable[int]] = ..., BKBNBIPFBCF: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., IEJPGHNLIDB: _Optional[int] = ..., BDCBLNLCAGE: bool = ..., GLKNGDDNOCN: bool = ..., IGBDOEBPPHO: _Optional[int] = ..., OBCLCJEJIML: _Optional[float] = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
