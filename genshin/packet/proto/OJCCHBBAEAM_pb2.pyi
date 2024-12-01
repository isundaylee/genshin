from genshin.packet.proto import LKDPHEFMBFM_pb2 as _LKDPHEFMBFM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OJCCHBBAEAM(_message.Message):
    __slots__ = ("CJIIEIOGBFO", "ILJHOELIJPF", "CAEONIPLBJC")
    CJIIEIOGBFO_FIELD_NUMBER: _ClassVar[int]
    ILJHOELIJPF_FIELD_NUMBER: _ClassVar[int]
    CAEONIPLBJC_FIELD_NUMBER: _ClassVar[int]
    CJIIEIOGBFO: _containers.RepeatedScalarFieldContainer[int]
    ILJHOELIJPF: _containers.RepeatedCompositeFieldContainer[_LKDPHEFMBFM_pb2.LKDPHEFMBFM]
    CAEONIPLBJC: int
    def __init__(self, CJIIEIOGBFO: _Optional[_Iterable[int]] = ..., ILJHOELIJPF: _Optional[_Iterable[_Union[_LKDPHEFMBFM_pb2.LKDPHEFMBFM, _Mapping]]] = ..., CAEONIPLBJC: _Optional[int] = ...) -> None: ...
