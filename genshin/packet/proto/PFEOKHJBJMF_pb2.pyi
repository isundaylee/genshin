from genshin.packet.proto import OFCLOOBNFGL_pb2 as _OFCLOOBNFGL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PFEOKHJBJMF(_message.Message):
    __slots__ = ("IECBCFCICOJ", "IOGJLEAMHCA", "EACIBINCAEI", "PGDGNMGCEKM")
    IECBCFCICOJ_FIELD_NUMBER: _ClassVar[int]
    IOGJLEAMHCA_FIELD_NUMBER: _ClassVar[int]
    EACIBINCAEI_FIELD_NUMBER: _ClassVar[int]
    PGDGNMGCEKM_FIELD_NUMBER: _ClassVar[int]
    IECBCFCICOJ: _containers.RepeatedCompositeFieldContainer[_OFCLOOBNFGL_pb2.OFCLOOBNFGL]
    IOGJLEAMHCA: _containers.RepeatedScalarFieldContainer[int]
    EACIBINCAEI: int
    PGDGNMGCEKM: bool
    def __init__(self, IECBCFCICOJ: _Optional[_Iterable[_Union[_OFCLOOBNFGL_pb2.OFCLOOBNFGL, _Mapping]]] = ..., IOGJLEAMHCA: _Optional[_Iterable[int]] = ..., EACIBINCAEI: _Optional[int] = ..., PGDGNMGCEKM: bool = ...) -> None: ...
