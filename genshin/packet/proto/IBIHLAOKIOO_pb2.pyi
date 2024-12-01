from genshin.packet.proto import MKPOEFOILGB_pb2 as _MKPOEFOILGB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IBIHLAOKIOO(_message.Message):
    __slots__ = ("FAGJDJIGLON", "OMENIAMEDCE", "KODNAAGLJDL", "ONHJABOEKHB", "KNGJHMLLCNP", "ODCMKOFFKKL")
    FAGJDJIGLON_FIELD_NUMBER: _ClassVar[int]
    OMENIAMEDCE_FIELD_NUMBER: _ClassVar[int]
    KODNAAGLJDL_FIELD_NUMBER: _ClassVar[int]
    ONHJABOEKHB_FIELD_NUMBER: _ClassVar[int]
    KNGJHMLLCNP_FIELD_NUMBER: _ClassVar[int]
    ODCMKOFFKKL_FIELD_NUMBER: _ClassVar[int]
    FAGJDJIGLON: _containers.RepeatedCompositeFieldContainer[_MKPOEFOILGB_pb2.MKPOEFOILGB]
    OMENIAMEDCE: bool
    KODNAAGLJDL: bool
    ONHJABOEKHB: int
    KNGJHMLLCNP: int
    ODCMKOFFKKL: int
    def __init__(self, FAGJDJIGLON: _Optional[_Iterable[_Union[_MKPOEFOILGB_pb2.MKPOEFOILGB, _Mapping]]] = ..., OMENIAMEDCE: bool = ..., KODNAAGLJDL: bool = ..., ONHJABOEKHB: _Optional[int] = ..., KNGJHMLLCNP: _Optional[int] = ..., ODCMKOFFKKL: _Optional[int] = ...) -> None: ...
