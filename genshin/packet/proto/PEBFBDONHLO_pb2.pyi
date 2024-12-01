from genshin.packet.proto import NFONHFAMDNE_pb2 as _NFONHFAMDNE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PEBFBDONHLO(_message.Message):
    __slots__ = ("ANCFLFIPDEI", "JHLBPPFGGPG")
    ANCFLFIPDEI_FIELD_NUMBER: _ClassVar[int]
    JHLBPPFGGPG_FIELD_NUMBER: _ClassVar[int]
    ANCFLFIPDEI: _containers.RepeatedScalarFieldContainer[_NFONHFAMDNE_pb2.NFONHFAMDNE]
    JHLBPPFGGPG: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ANCFLFIPDEI: _Optional[_Iterable[_Union[_NFONHFAMDNE_pb2.NFONHFAMDNE, str]]] = ..., JHLBPPFGGPG: _Optional[_Iterable[int]] = ...) -> None: ...
