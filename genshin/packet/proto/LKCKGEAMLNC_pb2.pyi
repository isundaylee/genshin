from genshin.packet.proto import JKGOMDDEPHJ_pb2 as _JKGOMDDEPHJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LKCKGEAMLNC(_message.Message):
    __slots__ = ("IEDIIPBBNDG", "PHOAEHGEALL", "OIMIJPCOOCM", "GGONBAHLADL")
    IEDIIPBBNDG_FIELD_NUMBER: _ClassVar[int]
    PHOAEHGEALL_FIELD_NUMBER: _ClassVar[int]
    OIMIJPCOOCM_FIELD_NUMBER: _ClassVar[int]
    GGONBAHLADL_FIELD_NUMBER: _ClassVar[int]
    IEDIIPBBNDG: _containers.RepeatedScalarFieldContainer[int]
    PHOAEHGEALL: _containers.RepeatedScalarFieldContainer[int]
    OIMIJPCOOCM: _containers.RepeatedScalarFieldContainer[int]
    GGONBAHLADL: _containers.RepeatedCompositeFieldContainer[_JKGOMDDEPHJ_pb2.JKGOMDDEPHJ]
    def __init__(self, IEDIIPBBNDG: _Optional[_Iterable[int]] = ..., PHOAEHGEALL: _Optional[_Iterable[int]] = ..., OIMIJPCOOCM: _Optional[_Iterable[int]] = ..., GGONBAHLADL: _Optional[_Iterable[_Union[_JKGOMDDEPHJ_pb2.JKGOMDDEPHJ, _Mapping]]] = ...) -> None: ...
