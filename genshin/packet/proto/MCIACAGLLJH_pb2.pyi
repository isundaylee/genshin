from genshin.packet.proto import JOKPHKNIFID_pb2 as _JOKPHKNIFID_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MCIACAGLLJH(_message.Message):
    __slots__ = ("KGMFMFGLLKA", "PGCKHIGJBFE", "KCFDPKKBECP")
    KGMFMFGLLKA_FIELD_NUMBER: _ClassVar[int]
    PGCKHIGJBFE_FIELD_NUMBER: _ClassVar[int]
    KCFDPKKBECP_FIELD_NUMBER: _ClassVar[int]
    KGMFMFGLLKA: _containers.RepeatedCompositeFieldContainer[_JOKPHKNIFID_pb2.JOKPHKNIFID]
    PGCKHIGJBFE: _containers.RepeatedScalarFieldContainer[int]
    KCFDPKKBECP: bool
    def __init__(self, KGMFMFGLLKA: _Optional[_Iterable[_Union[_JOKPHKNIFID_pb2.JOKPHKNIFID, _Mapping]]] = ..., PGCKHIGJBFE: _Optional[_Iterable[int]] = ..., KCFDPKKBECP: bool = ...) -> None: ...
