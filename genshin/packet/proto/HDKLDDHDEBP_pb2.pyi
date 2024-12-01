from genshin.packet.proto import AJMIMBMCABE_pb2 as _AJMIMBMCABE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HDKLDDHDEBP(_message.Message):
    __slots__ = ("BBOPFHAODOP", "HGGEHLMHKMP", "FINAHGLFHAG", "EAIPGEMKNPO")
    BBOPFHAODOP_FIELD_NUMBER: _ClassVar[int]
    HGGEHLMHKMP_FIELD_NUMBER: _ClassVar[int]
    FINAHGLFHAG_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    BBOPFHAODOP: _containers.RepeatedCompositeFieldContainer[_AJMIMBMCABE_pb2.AJMIMBMCABE]
    HGGEHLMHKMP: int
    FINAHGLFHAG: int
    EAIPGEMKNPO: int
    def __init__(self, BBOPFHAODOP: _Optional[_Iterable[_Union[_AJMIMBMCABE_pb2.AJMIMBMCABE, _Mapping]]] = ..., HGGEHLMHKMP: _Optional[int] = ..., FINAHGLFHAG: _Optional[int] = ..., EAIPGEMKNPO: _Optional[int] = ...) -> None: ...
