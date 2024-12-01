from genshin.packet.proto import PPJGPBJFEDB_pb2 as _PPJGPBJFEDB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AFDNKLDIHKD(_message.Message):
    __slots__ = ("FCFOJEGMOLM", "DMMJILKHDIM", "CFNKIAEELHN")
    FCFOJEGMOLM_FIELD_NUMBER: _ClassVar[int]
    DMMJILKHDIM_FIELD_NUMBER: _ClassVar[int]
    CFNKIAEELHN_FIELD_NUMBER: _ClassVar[int]
    FCFOJEGMOLM: _containers.RepeatedCompositeFieldContainer[_PPJGPBJFEDB_pb2.PPJGPBJFEDB]
    DMMJILKHDIM: _containers.RepeatedScalarFieldContainer[int]
    CFNKIAEELHN: int
    def __init__(self, FCFOJEGMOLM: _Optional[_Iterable[_Union[_PPJGPBJFEDB_pb2.PPJGPBJFEDB, _Mapping]]] = ..., DMMJILKHDIM: _Optional[_Iterable[int]] = ..., CFNKIAEELHN: _Optional[int] = ...) -> None: ...
