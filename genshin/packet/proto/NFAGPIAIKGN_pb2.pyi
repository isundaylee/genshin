from genshin.packet.proto import KNMPNCPBMMP_pb2 as _KNMPNCPBMMP_pb2
from genshin.packet.proto import CGACLDGEJJA_pb2 as _CGACLDGEJJA_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NFAGPIAIKGN(_message.Message):
    __slots__ = ("PBDCLALKDAB", "GNEOLEOJLFE", "HIJIIOLCKKI")
    PBDCLALKDAB_FIELD_NUMBER: _ClassVar[int]
    GNEOLEOJLFE_FIELD_NUMBER: _ClassVar[int]
    HIJIIOLCKKI_FIELD_NUMBER: _ClassVar[int]
    PBDCLALKDAB: _KNMPNCPBMMP_pb2.KNMPNCPBMMP
    GNEOLEOJLFE: _CGACLDGEJJA_pb2.CGACLDGEJJA
    HIJIIOLCKKI: int
    def __init__(self, PBDCLALKDAB: _Optional[_Union[_KNMPNCPBMMP_pb2.KNMPNCPBMMP, _Mapping]] = ..., GNEOLEOJLFE: _Optional[_Union[_CGACLDGEJJA_pb2.CGACLDGEJJA, _Mapping]] = ..., HIJIIOLCKKI: _Optional[int] = ...) -> None: ...
