from genshin.packet.proto import PINOGOECNFA_pb2 as _PINOGOECNFA_pb2
from genshin.packet.proto import PNFGMCACFNI_pb2 as _PNFGMCACFNI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AEPFMAPEHGD(_message.Message):
    __slots__ = ("IBAOLDBFOMP", "LHIKANCIHPG", "CFFMDKNINHD", "EJNINFFFKJP", "ALGDDKOLEOM")
    IBAOLDBFOMP_FIELD_NUMBER: _ClassVar[int]
    LHIKANCIHPG_FIELD_NUMBER: _ClassVar[int]
    CFFMDKNINHD_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    ALGDDKOLEOM_FIELD_NUMBER: _ClassVar[int]
    IBAOLDBFOMP: _containers.RepeatedCompositeFieldContainer[_PINOGOECNFA_pb2.PINOGOECNFA]
    LHIKANCIHPG: _containers.RepeatedCompositeFieldContainer[_PNFGMCACFNI_pb2.PNFGMCACFNI]
    CFFMDKNINHD: int
    EJNINFFFKJP: int
    ALGDDKOLEOM: int
    def __init__(self, IBAOLDBFOMP: _Optional[_Iterable[_Union[_PINOGOECNFA_pb2.PINOGOECNFA, _Mapping]]] = ..., LHIKANCIHPG: _Optional[_Iterable[_Union[_PNFGMCACFNI_pb2.PNFGMCACFNI, _Mapping]]] = ..., CFFMDKNINHD: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ..., ALGDDKOLEOM: _Optional[int] = ...) -> None: ...
