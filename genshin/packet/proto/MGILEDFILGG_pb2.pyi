from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from genshin.packet.proto import HMIDOBJFNFM_pb2 as _HMIDOBJFNFM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MGILEDFILGG(_message.Message):
    __slots__ = ("MEIKGBOLDGH", "FAGJDJIGLON", "KNGJHMLLCNP", "ONHJABOEKHB", "MPNJAOCKMAH", "ODCMKOFFKKL", "KODNAAGLJDL", "OMENIAMEDCE")
    MEIKGBOLDGH_FIELD_NUMBER: _ClassVar[int]
    FAGJDJIGLON_FIELD_NUMBER: _ClassVar[int]
    KNGJHMLLCNP_FIELD_NUMBER: _ClassVar[int]
    ONHJABOEKHB_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    ODCMKOFFKKL_FIELD_NUMBER: _ClassVar[int]
    KODNAAGLJDL_FIELD_NUMBER: _ClassVar[int]
    OMENIAMEDCE_FIELD_NUMBER: _ClassVar[int]
    MEIKGBOLDGH: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    FAGJDJIGLON: _containers.RepeatedCompositeFieldContainer[_HMIDOBJFNFM_pb2.HMIDOBJFNFM]
    KNGJHMLLCNP: int
    ONHJABOEKHB: int
    MPNJAOCKMAH: int
    ODCMKOFFKKL: int
    KODNAAGLJDL: bool
    OMENIAMEDCE: bool
    def __init__(self, MEIKGBOLDGH: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., FAGJDJIGLON: _Optional[_Iterable[_Union[_HMIDOBJFNFM_pb2.HMIDOBJFNFM, _Mapping]]] = ..., KNGJHMLLCNP: _Optional[int] = ..., ONHJABOEKHB: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ..., ODCMKOFFKKL: _Optional[int] = ..., KODNAAGLJDL: bool = ..., OMENIAMEDCE: bool = ...) -> None: ...
