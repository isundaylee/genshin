from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PKIEGAJBPPD(_message.Message):
    __slots__ = ("OHGEMJLBBGI", "FIKLBLMACIB", "IBJINLCKJAC", "NKMBBFHGMKB", "guid")
    OHGEMJLBBGI_FIELD_NUMBER: _ClassVar[int]
    FIKLBLMACIB_FIELD_NUMBER: _ClassVar[int]
    IBJINLCKJAC_FIELD_NUMBER: _ClassVar[int]
    NKMBBFHGMKB_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    OHGEMJLBBGI: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    FIKLBLMACIB: int
    IBJINLCKJAC: bool
    NKMBBFHGMKB: bool
    guid: int
    def __init__(self, OHGEMJLBBGI: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., FIKLBLMACIB: _Optional[int] = ..., IBJINLCKJAC: bool = ..., NKMBBFHGMKB: bool = ..., guid: _Optional[int] = ...) -> None: ...
