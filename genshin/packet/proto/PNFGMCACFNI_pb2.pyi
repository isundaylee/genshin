from genshin.packet.proto import PINOGOECNFA_pb2 as _PINOGOECNFA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PNFGMCACFNI(_message.Message):
    __slots__ = ("IBAOLDBFOMP", "CFFMDKNINHD", "IGBDOEBPPHO", "ALGDDKOLEOM")
    IBAOLDBFOMP_FIELD_NUMBER: _ClassVar[int]
    CFFMDKNINHD_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    ALGDDKOLEOM_FIELD_NUMBER: _ClassVar[int]
    IBAOLDBFOMP: _containers.RepeatedCompositeFieldContainer[_PINOGOECNFA_pb2.PINOGOECNFA]
    CFFMDKNINHD: int
    IGBDOEBPPHO: int
    ALGDDKOLEOM: int
    def __init__(self, IBAOLDBFOMP: _Optional[_Iterable[_Union[_PINOGOECNFA_pb2.PINOGOECNFA, _Mapping]]] = ..., CFFMDKNINHD: _Optional[int] = ..., IGBDOEBPPHO: _Optional[int] = ..., ALGDDKOLEOM: _Optional[int] = ...) -> None: ...
