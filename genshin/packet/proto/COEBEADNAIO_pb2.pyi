from genshin.packet.proto import KNMPNCPBMMP_pb2 as _KNMPNCPBMMP_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class COEBEADNAIO(_message.Message):
    __slots__ = ("PBDCLALKDAB", "HIJIIOLCKKI", "KBNHDNPJJBH")
    PBDCLALKDAB_FIELD_NUMBER: _ClassVar[int]
    HIJIIOLCKKI_FIELD_NUMBER: _ClassVar[int]
    KBNHDNPJJBH_FIELD_NUMBER: _ClassVar[int]
    PBDCLALKDAB: _KNMPNCPBMMP_pb2.KNMPNCPBMMP
    HIJIIOLCKKI: int
    KBNHDNPJJBH: int
    def __init__(self, PBDCLALKDAB: _Optional[_Union[_KNMPNCPBMMP_pb2.KNMPNCPBMMP, _Mapping]] = ..., HIJIIOLCKKI: _Optional[int] = ..., KBNHDNPJJBH: _Optional[int] = ...) -> None: ...
