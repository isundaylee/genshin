from genshin.packet.proto import LGIDOEBEPCL_pb2 as _LGIDOEBEPCL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GPPOMEGKDFI(_message.Message):
    __slots__ = ("HOBAIDKKPLG", "PNMCKBOBBHA", "HHNBGONEIHH", "BGICAKMCBMH")
    HOBAIDKKPLG_FIELD_NUMBER: _ClassVar[int]
    PNMCKBOBBHA_FIELD_NUMBER: _ClassVar[int]
    HHNBGONEIHH_FIELD_NUMBER: _ClassVar[int]
    BGICAKMCBMH_FIELD_NUMBER: _ClassVar[int]
    HOBAIDKKPLG: _containers.RepeatedScalarFieldContainer[int]
    PNMCKBOBBHA: _containers.RepeatedCompositeFieldContainer[_LGIDOEBEPCL_pb2.LGIDOEBEPCL]
    HHNBGONEIHH: bool
    BGICAKMCBMH: bool
    def __init__(self, HOBAIDKKPLG: _Optional[_Iterable[int]] = ..., PNMCKBOBBHA: _Optional[_Iterable[_Union[_LGIDOEBEPCL_pb2.LGIDOEBEPCL, _Mapping]]] = ..., HHNBGONEIHH: bool = ..., BGICAKMCBMH: bool = ...) -> None: ...
