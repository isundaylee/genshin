from genshin.packet.proto import KOKDNEPGGBH_pb2 as _KOKDNEPGGBH_pb2
from genshin.packet.proto import GAGHIFFFHOI_pb2 as _GAGHIFFFHOI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KCICAHCPBGB(_message.Message):
    __slots__ = ("CFMGHCAKEAE", "GIDLEKLAHAP", "HGGKGCHKCFB", "PHNIDOPEBAH", "JKPCJABBGJB", "MMABHBCILDG", "OAJOOBGHAGM")
    CFMGHCAKEAE_FIELD_NUMBER: _ClassVar[int]
    GIDLEKLAHAP_FIELD_NUMBER: _ClassVar[int]
    HGGKGCHKCFB_FIELD_NUMBER: _ClassVar[int]
    PHNIDOPEBAH_FIELD_NUMBER: _ClassVar[int]
    JKPCJABBGJB_FIELD_NUMBER: _ClassVar[int]
    MMABHBCILDG_FIELD_NUMBER: _ClassVar[int]
    OAJOOBGHAGM_FIELD_NUMBER: _ClassVar[int]
    CFMGHCAKEAE: _containers.RepeatedCompositeFieldContainer[_KOKDNEPGGBH_pb2.KOKDNEPGGBH]
    GIDLEKLAHAP: _containers.RepeatedCompositeFieldContainer[_GAGHIFFFHOI_pb2.GAGHIFFFHOI]
    HGGKGCHKCFB: _containers.RepeatedScalarFieldContainer[int]
    PHNIDOPEBAH: _containers.RepeatedScalarFieldContainer[int]
    JKPCJABBGJB: int
    MMABHBCILDG: int
    OAJOOBGHAGM: int
    def __init__(self, CFMGHCAKEAE: _Optional[_Iterable[_Union[_KOKDNEPGGBH_pb2.KOKDNEPGGBH, _Mapping]]] = ..., GIDLEKLAHAP: _Optional[_Iterable[_Union[_GAGHIFFFHOI_pb2.GAGHIFFFHOI, _Mapping]]] = ..., HGGKGCHKCFB: _Optional[_Iterable[int]] = ..., PHNIDOPEBAH: _Optional[_Iterable[int]] = ..., JKPCJABBGJB: _Optional[int] = ..., MMABHBCILDG: _Optional[int] = ..., OAJOOBGHAGM: _Optional[int] = ...) -> None: ...
