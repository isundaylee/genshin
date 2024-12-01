from genshin.packet.proto import PKJMCKIDJFL_pb2 as _PKJMCKIDJFL_pb2
from genshin.packet.proto import FJINCAKIFKG_pb2 as _FJINCAKIFKG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AKLLEMMHOLI(_message.Message):
    __slots__ = ("MBBDPMPHNGH", "NLAAAAKIOJB", "CGIKOFOCCIE", "MDKPOJCCEJJ", "HIMCEFBJCLB", "MPFLDFDOGAI")
    MBBDPMPHNGH_FIELD_NUMBER: _ClassVar[int]
    NLAAAAKIOJB_FIELD_NUMBER: _ClassVar[int]
    CGIKOFOCCIE_FIELD_NUMBER: _ClassVar[int]
    MDKPOJCCEJJ_FIELD_NUMBER: _ClassVar[int]
    HIMCEFBJCLB_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    MBBDPMPHNGH: _containers.RepeatedScalarFieldContainer[int]
    NLAAAAKIOJB: _containers.RepeatedScalarFieldContainer[int]
    CGIKOFOCCIE: _containers.RepeatedCompositeFieldContainer[_PKJMCKIDJFL_pb2.PKJMCKIDJFL]
    MDKPOJCCEJJ: _containers.RepeatedCompositeFieldContainer[_FJINCAKIFKG_pb2.FJINCAKIFKG]
    HIMCEFBJCLB: bool
    MPFLDFDOGAI: bool
    def __init__(self, MBBDPMPHNGH: _Optional[_Iterable[int]] = ..., NLAAAAKIOJB: _Optional[_Iterable[int]] = ..., CGIKOFOCCIE: _Optional[_Iterable[_Union[_PKJMCKIDJFL_pb2.PKJMCKIDJFL, _Mapping]]] = ..., MDKPOJCCEJJ: _Optional[_Iterable[_Union[_FJINCAKIFKG_pb2.FJINCAKIFKG, _Mapping]]] = ..., HIMCEFBJCLB: bool = ..., MPFLDFDOGAI: bool = ...) -> None: ...
