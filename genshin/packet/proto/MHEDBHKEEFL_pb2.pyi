from genshin.packet.proto import StoreType_pb2 as _StoreType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MHEDBHKEEFL(_message.Message):
    __slots__ = ("weight_limit", "PCMELFFPEGC", "GGIGOODBBKI", "MLMPLAOMLNK", "store_type", "LFEDHEOGICP")
    WEIGHT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PCMELFFPEGC_FIELD_NUMBER: _ClassVar[int]
    GGIGOODBBKI_FIELD_NUMBER: _ClassVar[int]
    MLMPLAOMLNK_FIELD_NUMBER: _ClassVar[int]
    STORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LFEDHEOGICP_FIELD_NUMBER: _ClassVar[int]
    weight_limit: int
    PCMELFFPEGC: int
    GGIGOODBBKI: int
    MLMPLAOMLNK: int
    store_type: _StoreType_pb2.StoreType
    LFEDHEOGICP: int
    def __init__(self, weight_limit: _Optional[int] = ..., PCMELFFPEGC: _Optional[int] = ..., GGIGOODBBKI: _Optional[int] = ..., MLMPLAOMLNK: _Optional[int] = ..., store_type: _Optional[_Union[_StoreType_pb2.StoreType, str]] = ..., LFEDHEOGICP: _Optional[int] = ...) -> None: ...
