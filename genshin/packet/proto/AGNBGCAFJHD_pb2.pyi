from genshin.packet.proto import GAFKAPLOFDB_pb2 as _GAFKAPLOFDB_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AGNBGCAFJHD(_message.Message):
    __slots__ = ("MNKNAJCDNBK", "KJPECHHMEKN", "FKCLBEINJGH", "MBBKAENBCKD")
    MNKNAJCDNBK_FIELD_NUMBER: _ClassVar[int]
    KJPECHHMEKN_FIELD_NUMBER: _ClassVar[int]
    FKCLBEINJGH_FIELD_NUMBER: _ClassVar[int]
    MBBKAENBCKD_FIELD_NUMBER: _ClassVar[int]
    MNKNAJCDNBK: bytes
    KJPECHHMEKN: _GAFKAPLOFDB_pb2.GAFKAPLOFDB
    FKCLBEINJGH: int
    MBBKAENBCKD: int
    def __init__(self, MNKNAJCDNBK: _Optional[bytes] = ..., KJPECHHMEKN: _Optional[_Union[_GAFKAPLOFDB_pb2.GAFKAPLOFDB, str]] = ..., FKCLBEINJGH: _Optional[int] = ..., MBBKAENBCKD: _Optional[int] = ...) -> None: ...
