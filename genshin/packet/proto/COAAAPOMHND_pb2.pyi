from genshin.packet.proto import MPGGMJODJAO_pb2 as _MPGGMJODJAO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class COAAAPOMHND(_message.Message):
    __slots__ = ("NBJNBCMHJFB", "NJOPAJDOBCE", "EJNINFFFKJP")
    NBJNBCMHJFB_FIELD_NUMBER: _ClassVar[int]
    NJOPAJDOBCE_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    NBJNBCMHJFB: _containers.RepeatedScalarFieldContainer[int]
    NJOPAJDOBCE: _containers.RepeatedCompositeFieldContainer[_MPGGMJODJAO_pb2.MPGGMJODJAO]
    EJNINFFFKJP: int
    def __init__(self, NBJNBCMHJFB: _Optional[_Iterable[int]] = ..., NJOPAJDOBCE: _Optional[_Iterable[_Union[_MPGGMJODJAO_pb2.MPGGMJODJAO, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
