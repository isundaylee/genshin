from genshin.packet.proto import JIIOMJGCKLO_pb2 as _JIIOMJGCKLO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KAEGAFABHLL(_message.Message):
    __slots__ = ("HILLLCLAILE", "EJNINFFFKJP", "NCCPPHNNPBF")
    HILLLCLAILE_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    HILLLCLAILE: _containers.RepeatedCompositeFieldContainer[_JIIOMJGCKLO_pb2.JIIOMJGCKLO]
    EJNINFFFKJP: int
    NCCPPHNNPBF: int
    def __init__(self, HILLLCLAILE: _Optional[_Iterable[_Union[_JIIOMJGCKLO_pb2.JIIOMJGCKLO, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., NCCPPHNNPBF: _Optional[int] = ...) -> None: ...
