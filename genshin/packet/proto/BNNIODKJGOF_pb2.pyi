from genshin.packet.proto import JIIOMJGCKLO_pb2 as _JIIOMJGCKLO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BNNIODKJGOF(_message.Message):
    __slots__ = ("DGDCHJKCJIP", "HILLLCLAILE", "EJNINFFFKJP", "GCACPOMLGMJ")
    DGDCHJKCJIP_FIELD_NUMBER: _ClassVar[int]
    HILLLCLAILE_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    GCACPOMLGMJ_FIELD_NUMBER: _ClassVar[int]
    DGDCHJKCJIP: _containers.RepeatedScalarFieldContainer[int]
    HILLLCLAILE: _containers.RepeatedCompositeFieldContainer[_JIIOMJGCKLO_pb2.JIIOMJGCKLO]
    EJNINFFFKJP: int
    GCACPOMLGMJ: bool
    def __init__(self, DGDCHJKCJIP: _Optional[_Iterable[int]] = ..., HILLLCLAILE: _Optional[_Iterable[_Union[_JIIOMJGCKLO_pb2.JIIOMJGCKLO, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., GCACPOMLGMJ: bool = ...) -> None: ...
