from genshin.packet.proto import MPMGNGLJGJP_pb2 as _MPMGNGLJGJP_pb2
from genshin.packet.proto import NHMFHFJPPKM_pb2 as _NHMFHFJPPKM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PMLBOKPCDMG(_message.Message):
    __slots__ = ("MBDHJJOHCKO", "HNBFDMAMJKO", "JBFBEPKMBDM", "FGHMMAAEOLA")
    MBDHJJOHCKO_FIELD_NUMBER: _ClassVar[int]
    HNBFDMAMJKO_FIELD_NUMBER: _ClassVar[int]
    JBFBEPKMBDM_FIELD_NUMBER: _ClassVar[int]
    FGHMMAAEOLA_FIELD_NUMBER: _ClassVar[int]
    MBDHJJOHCKO: _containers.RepeatedCompositeFieldContainer[_MPMGNGLJGJP_pb2.MPMGNGLJGJP]
    HNBFDMAMJKO: _containers.RepeatedCompositeFieldContainer[_NHMFHFJPPKM_pb2.NHMFHFJPPKM]
    JBFBEPKMBDM: int
    FGHMMAAEOLA: int
    def __init__(self, MBDHJJOHCKO: _Optional[_Iterable[_Union[_MPMGNGLJGJP_pb2.MPMGNGLJGJP, _Mapping]]] = ..., HNBFDMAMJKO: _Optional[_Iterable[_Union[_NHMFHFJPPKM_pb2.NHMFHFJPPKM, _Mapping]]] = ..., JBFBEPKMBDM: _Optional[int] = ..., FGHMMAAEOLA: _Optional[int] = ...) -> None: ...
