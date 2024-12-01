from genshin.packet.proto import GFNEAFEFCCL_pb2 as _GFNEAFEFCCL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ABGKEDBGBLN(_message.Message):
    __slots__ = ("JLNAKOLCDGN", "GLKNGDDNOCN", "LBEINAHAHKA")
    JLNAKOLCDGN_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    LBEINAHAHKA_FIELD_NUMBER: _ClassVar[int]
    JLNAKOLCDGN: _containers.RepeatedCompositeFieldContainer[_GFNEAFEFCCL_pb2.GFNEAFEFCCL]
    GLKNGDDNOCN: bool
    LBEINAHAHKA: int
    def __init__(self, JLNAKOLCDGN: _Optional[_Iterable[_Union[_GFNEAFEFCCL_pb2.GFNEAFEFCCL, _Mapping]]] = ..., GLKNGDDNOCN: bool = ..., LBEINAHAHKA: _Optional[int] = ...) -> None: ...
