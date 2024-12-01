from genshin.packet.proto import EINAPLINOFB_pb2 as _EINAPLINOFB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PIKDLMGGINC(_message.Message):
    __slots__ = ("CLKEHKJIINL", "MPFLDFDOGAI", "HENIIKDCDPK")
    CLKEHKJIINL_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    HENIIKDCDPK_FIELD_NUMBER: _ClassVar[int]
    CLKEHKJIINL: _containers.RepeatedCompositeFieldContainer[_EINAPLINOFB_pb2.EINAPLINOFB]
    MPFLDFDOGAI: bool
    HENIIKDCDPK: int
    def __init__(self, CLKEHKJIINL: _Optional[_Iterable[_Union[_EINAPLINOFB_pb2.EINAPLINOFB, _Mapping]]] = ..., MPFLDFDOGAI: bool = ..., HENIIKDCDPK: _Optional[int] = ...) -> None: ...
