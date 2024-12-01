from genshin.packet.proto import POBOBNIMGLK_pb2 as _POBOBNIMGLK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EJMMNHEFOFG(_message.Message):
    __slots__ = ("JPAHJDDEILM", "MPFLDFDOGAI")
    JPAHJDDEILM_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    JPAHJDDEILM: _containers.RepeatedCompositeFieldContainer[_POBOBNIMGLK_pb2.POBOBNIMGLK]
    MPFLDFDOGAI: bool
    def __init__(self, JPAHJDDEILM: _Optional[_Iterable[_Union[_POBOBNIMGLK_pb2.POBOBNIMGLK, _Mapping]]] = ..., MPFLDFDOGAI: bool = ...) -> None: ...
