from genshin.packet.proto import PLGMIDNFDFN_pb2 as _PLGMIDNFDFN_pb2
from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AAEEAPMIKPF(_message.Message):
    __slots__ = ("CLJIKPEPLEC", "FAGJDJIGLON", "MEIKGBOLDGH", "KKPPJFKDDEP", "KODNAAGLJDL", "BPDLJHGNNGD", "JIMELGDJMLF", "JABGACILLEC", "POAFICPFPCJ")
    CLJIKPEPLEC_FIELD_NUMBER: _ClassVar[int]
    FAGJDJIGLON_FIELD_NUMBER: _ClassVar[int]
    MEIKGBOLDGH_FIELD_NUMBER: _ClassVar[int]
    KKPPJFKDDEP_FIELD_NUMBER: _ClassVar[int]
    KODNAAGLJDL_FIELD_NUMBER: _ClassVar[int]
    BPDLJHGNNGD_FIELD_NUMBER: _ClassVar[int]
    JIMELGDJMLF_FIELD_NUMBER: _ClassVar[int]
    JABGACILLEC_FIELD_NUMBER: _ClassVar[int]
    POAFICPFPCJ_FIELD_NUMBER: _ClassVar[int]
    CLJIKPEPLEC: _containers.RepeatedScalarFieldContainer[int]
    FAGJDJIGLON: _containers.RepeatedCompositeFieldContainer[_PLGMIDNFDFN_pb2.PLGMIDNFDFN]
    MEIKGBOLDGH: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    KKPPJFKDDEP: int
    KODNAAGLJDL: bool
    BPDLJHGNNGD: bool
    JIMELGDJMLF: int
    JABGACILLEC: int
    POAFICPFPCJ: int
    def __init__(self, CLJIKPEPLEC: _Optional[_Iterable[int]] = ..., FAGJDJIGLON: _Optional[_Iterable[_Union[_PLGMIDNFDFN_pb2.PLGMIDNFDFN, _Mapping]]] = ..., MEIKGBOLDGH: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., KKPPJFKDDEP: _Optional[int] = ..., KODNAAGLJDL: bool = ..., BPDLJHGNNGD: bool = ..., JIMELGDJMLF: _Optional[int] = ..., JABGACILLEC: _Optional[int] = ..., POAFICPFPCJ: _Optional[int] = ...) -> None: ...
