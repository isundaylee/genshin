from genshin.packet.proto import CKNODNHICOL_pb2 as _CKNODNHICOL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ICKFOBLBMFP(_message.Message):
    __slots__ = ("BJJPECNJIJE", "GAINCCNCANO", "EJNINFFFKJP")
    BJJPECNJIJE_FIELD_NUMBER: _ClassVar[int]
    GAINCCNCANO_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    BJJPECNJIJE: _containers.RepeatedCompositeFieldContainer[_CKNODNHICOL_pb2.CKNODNHICOL]
    GAINCCNCANO: int
    EJNINFFFKJP: int
    def __init__(self, BJJPECNJIJE: _Optional[_Iterable[_Union[_CKNODNHICOL_pb2.CKNODNHICOL, _Mapping]]] = ..., GAINCCNCANO: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
