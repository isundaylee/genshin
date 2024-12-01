from genshin.packet.proto import KIBLANEDMOA_pb2 as _KIBLANEDMOA_pb2
from genshin.packet.proto import NCGPMHOIHHL_pb2 as _NCGPMHOIHHL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NFGBKNPJAIN(_message.Message):
    __slots__ = ("KABODNMEGEK", "OKKJCBOJAOD")
    KABODNMEGEK_FIELD_NUMBER: _ClassVar[int]
    OKKJCBOJAOD_FIELD_NUMBER: _ClassVar[int]
    KABODNMEGEK: _containers.RepeatedCompositeFieldContainer[_KIBLANEDMOA_pb2.KIBLANEDMOA]
    OKKJCBOJAOD: _NCGPMHOIHHL_pb2.NCGPMHOIHHL
    def __init__(self, KABODNMEGEK: _Optional[_Iterable[_Union[_KIBLANEDMOA_pb2.KIBLANEDMOA, _Mapping]]] = ..., OKKJCBOJAOD: _Optional[_Union[_NCGPMHOIHHL_pb2.NCGPMHOIHHL, _Mapping]] = ...) -> None: ...
