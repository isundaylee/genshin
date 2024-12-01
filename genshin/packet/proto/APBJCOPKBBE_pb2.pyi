from genshin.packet.proto import MDLJNANFJMC_pb2 as _MDLJNANFJMC_pb2
from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class APBJCOPKBBE(_message.Message):
    __slots__ = ("FAGJDJIGLON", "MEIKGBOLDGH", "GLKDKOJDNFE", "JABGACILLEC", "JIMELGDJMLF", "BPDLJHGNNGD", "HAEAOOFAJNG", "KNGJHMLLCNP", "IKDAJELLEAI", "POAFICPFPCJ")
    FAGJDJIGLON_FIELD_NUMBER: _ClassVar[int]
    MEIKGBOLDGH_FIELD_NUMBER: _ClassVar[int]
    GLKDKOJDNFE_FIELD_NUMBER: _ClassVar[int]
    JABGACILLEC_FIELD_NUMBER: _ClassVar[int]
    JIMELGDJMLF_FIELD_NUMBER: _ClassVar[int]
    BPDLJHGNNGD_FIELD_NUMBER: _ClassVar[int]
    HAEAOOFAJNG_FIELD_NUMBER: _ClassVar[int]
    KNGJHMLLCNP_FIELD_NUMBER: _ClassVar[int]
    IKDAJELLEAI_FIELD_NUMBER: _ClassVar[int]
    POAFICPFPCJ_FIELD_NUMBER: _ClassVar[int]
    FAGJDJIGLON: _containers.RepeatedCompositeFieldContainer[_MDLJNANFJMC_pb2.MDLJNANFJMC]
    MEIKGBOLDGH: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    GLKDKOJDNFE: _containers.RepeatedScalarFieldContainer[int]
    JABGACILLEC: int
    JIMELGDJMLF: int
    BPDLJHGNNGD: bool
    HAEAOOFAJNG: bool
    KNGJHMLLCNP: int
    IKDAJELLEAI: int
    POAFICPFPCJ: int
    def __init__(self, FAGJDJIGLON: _Optional[_Iterable[_Union[_MDLJNANFJMC_pb2.MDLJNANFJMC, _Mapping]]] = ..., MEIKGBOLDGH: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., GLKDKOJDNFE: _Optional[_Iterable[int]] = ..., JABGACILLEC: _Optional[int] = ..., JIMELGDJMLF: _Optional[int] = ..., BPDLJHGNNGD: bool = ..., HAEAOOFAJNG: bool = ..., KNGJHMLLCNP: _Optional[int] = ..., IKDAJELLEAI: _Optional[int] = ..., POAFICPFPCJ: _Optional[int] = ...) -> None: ...
