from genshin.packet.proto import PLIAJBGKCMD_pb2 as _PLIAJBGKCMD_pb2
from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EJEIEDAJKEE(_message.Message):
    __slots__ = ("FAGJDJIGLON", "CLJIKPEPLEC", "MEIKGBOLDGH", "BPDLJHGNNGD", "OMENIAMEDCE", "KODNAAGLJDL", "BILMACEFNPF", "JIMELGDJMLF", "KKPPJFKDDEP")
    FAGJDJIGLON_FIELD_NUMBER: _ClassVar[int]
    CLJIKPEPLEC_FIELD_NUMBER: _ClassVar[int]
    MEIKGBOLDGH_FIELD_NUMBER: _ClassVar[int]
    BPDLJHGNNGD_FIELD_NUMBER: _ClassVar[int]
    OMENIAMEDCE_FIELD_NUMBER: _ClassVar[int]
    KODNAAGLJDL_FIELD_NUMBER: _ClassVar[int]
    BILMACEFNPF_FIELD_NUMBER: _ClassVar[int]
    JIMELGDJMLF_FIELD_NUMBER: _ClassVar[int]
    KKPPJFKDDEP_FIELD_NUMBER: _ClassVar[int]
    FAGJDJIGLON: _containers.RepeatedCompositeFieldContainer[_PLIAJBGKCMD_pb2.PLIAJBGKCMD]
    CLJIKPEPLEC: _containers.RepeatedScalarFieldContainer[int]
    MEIKGBOLDGH: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    BPDLJHGNNGD: bool
    OMENIAMEDCE: bool
    KODNAAGLJDL: bool
    BILMACEFNPF: int
    JIMELGDJMLF: int
    KKPPJFKDDEP: int
    def __init__(self, FAGJDJIGLON: _Optional[_Iterable[_Union[_PLIAJBGKCMD_pb2.PLIAJBGKCMD, _Mapping]]] = ..., CLJIKPEPLEC: _Optional[_Iterable[int]] = ..., MEIKGBOLDGH: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., BPDLJHGNNGD: bool = ..., OMENIAMEDCE: bool = ..., KODNAAGLJDL: bool = ..., BILMACEFNPF: _Optional[int] = ..., JIMELGDJMLF: _Optional[int] = ..., KKPPJFKDDEP: _Optional[int] = ...) -> None: ...
