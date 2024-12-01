from genshin.packet.proto import JHKPMJJLLOF_pb2 as _JHKPMJJLLOF_pb2
from genshin.packet.proto import DCCLJIKDBFG_pb2 as _DCCLJIKDBFG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MCIGBDLJIFH(_message.Message):
    __slots__ = ("HINHOECHNFL", "LOOGLCJLADB", "GLKNGDDNOCN", "EAIPGEMKNPO", "IEJPGHNLIDB")
    HINHOECHNFL_FIELD_NUMBER: _ClassVar[int]
    LOOGLCJLADB_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    IEJPGHNLIDB_FIELD_NUMBER: _ClassVar[int]
    HINHOECHNFL: _JHKPMJJLLOF_pb2.JHKPMJJLLOF
    LOOGLCJLADB: _containers.RepeatedCompositeFieldContainer[_DCCLJIKDBFG_pb2.DCCLJIKDBFG]
    GLKNGDDNOCN: bool
    EAIPGEMKNPO: int
    IEJPGHNLIDB: int
    def __init__(self, HINHOECHNFL: _Optional[_Union[_JHKPMJJLLOF_pb2.JHKPMJJLLOF, _Mapping]] = ..., LOOGLCJLADB: _Optional[_Iterable[_Union[_DCCLJIKDBFG_pb2.DCCLJIKDBFG, _Mapping]]] = ..., GLKNGDDNOCN: bool = ..., EAIPGEMKNPO: _Optional[int] = ..., IEJPGHNLIDB: _Optional[int] = ...) -> None: ...
