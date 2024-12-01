from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from genshin.packet.proto import DLFIOIILGFN_pb2 as _DLFIOIILGFN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NLGIAHINBPB(_message.Message):
    __slots__ = ("GLKDKOJDNFE", "MEIKGBOLDGH", "FAGJDJIGLON", "JIMELGDJMLF", "HAEAOOFAJNG", "KNGJHMLLCNP", "KKPPJFKDDEP")
    GLKDKOJDNFE_FIELD_NUMBER: _ClassVar[int]
    MEIKGBOLDGH_FIELD_NUMBER: _ClassVar[int]
    FAGJDJIGLON_FIELD_NUMBER: _ClassVar[int]
    JIMELGDJMLF_FIELD_NUMBER: _ClassVar[int]
    HAEAOOFAJNG_FIELD_NUMBER: _ClassVar[int]
    KNGJHMLLCNP_FIELD_NUMBER: _ClassVar[int]
    KKPPJFKDDEP_FIELD_NUMBER: _ClassVar[int]
    GLKDKOJDNFE: _containers.RepeatedScalarFieldContainer[int]
    MEIKGBOLDGH: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    FAGJDJIGLON: _containers.RepeatedCompositeFieldContainer[_DLFIOIILGFN_pb2.DLFIOIILGFN]
    JIMELGDJMLF: int
    HAEAOOFAJNG: bool
    KNGJHMLLCNP: int
    KKPPJFKDDEP: int
    def __init__(self, GLKDKOJDNFE: _Optional[_Iterable[int]] = ..., MEIKGBOLDGH: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., FAGJDJIGLON: _Optional[_Iterable[_Union[_DLFIOIILGFN_pb2.DLFIOIILGFN, _Mapping]]] = ..., JIMELGDJMLF: _Optional[int] = ..., HAEAOOFAJNG: bool = ..., KNGJHMLLCNP: _Optional[int] = ..., KKPPJFKDDEP: _Optional[int] = ...) -> None: ...
