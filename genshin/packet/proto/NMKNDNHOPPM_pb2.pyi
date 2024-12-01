from genshin.packet.proto import AJMIMBMCABE_pb2 as _AJMIMBMCABE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NMKNDNHOPPM(_message.Message):
    __slots__ = ("BBOPFHAODOP", "NMAAPLDBBNI", "GLKNGDDNOCN", "EAIPGEMKNPO", "IEJPGHNLIDB")
    BBOPFHAODOP_FIELD_NUMBER: _ClassVar[int]
    NMAAPLDBBNI_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    IEJPGHNLIDB_FIELD_NUMBER: _ClassVar[int]
    BBOPFHAODOP: _containers.RepeatedCompositeFieldContainer[_AJMIMBMCABE_pb2.AJMIMBMCABE]
    NMAAPLDBBNI: int
    GLKNGDDNOCN: bool
    EAIPGEMKNPO: int
    IEJPGHNLIDB: int
    def __init__(self, BBOPFHAODOP: _Optional[_Iterable[_Union[_AJMIMBMCABE_pb2.AJMIMBMCABE, _Mapping]]] = ..., NMAAPLDBBNI: _Optional[int] = ..., GLKNGDDNOCN: bool = ..., EAIPGEMKNPO: _Optional[int] = ..., IEJPGHNLIDB: _Optional[int] = ...) -> None: ...
