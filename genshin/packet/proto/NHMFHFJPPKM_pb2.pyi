from genshin.packet.proto import GPHNLHKIJFC_pb2 as _GPHNLHKIJFC_pb2
from genshin.packet.proto import MPMGNGLJGJP_pb2 as _MPMGNGLJGJP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NHMFHFJPPKM(_message.Message):
    __slots__ = ("MPAMGDHBMGH", "BIPADACDOFI", "NJBFNIFMOKJ", "JOILDLJPNEC", "AHBIDIAELPL", "LFGCGEDEBGM", "KEJDLAEBHIF", "JMGEOCMBEKF", "DFANCLIKIOI", "PCJNMGGMLJE")
    MPAMGDHBMGH_FIELD_NUMBER: _ClassVar[int]
    BIPADACDOFI_FIELD_NUMBER: _ClassVar[int]
    NJBFNIFMOKJ_FIELD_NUMBER: _ClassVar[int]
    JOILDLJPNEC_FIELD_NUMBER: _ClassVar[int]
    AHBIDIAELPL_FIELD_NUMBER: _ClassVar[int]
    LFGCGEDEBGM_FIELD_NUMBER: _ClassVar[int]
    KEJDLAEBHIF_FIELD_NUMBER: _ClassVar[int]
    JMGEOCMBEKF_FIELD_NUMBER: _ClassVar[int]
    DFANCLIKIOI_FIELD_NUMBER: _ClassVar[int]
    PCJNMGGMLJE_FIELD_NUMBER: _ClassVar[int]
    MPAMGDHBMGH: _GPHNLHKIJFC_pb2.GPHNLHKIJFC
    BIPADACDOFI: _containers.RepeatedScalarFieldContainer[int]
    NJBFNIFMOKJ: _containers.RepeatedCompositeFieldContainer[_MPMGNGLJGJP_pb2.MPMGNGLJGJP]
    JOILDLJPNEC: int
    AHBIDIAELPL: int
    LFGCGEDEBGM: int
    KEJDLAEBHIF: int
    JMGEOCMBEKF: bool
    DFANCLIKIOI: bool
    PCJNMGGMLJE: int
    def __init__(self, MPAMGDHBMGH: _Optional[_Union[_GPHNLHKIJFC_pb2.GPHNLHKIJFC, _Mapping]] = ..., BIPADACDOFI: _Optional[_Iterable[int]] = ..., NJBFNIFMOKJ: _Optional[_Iterable[_Union[_MPMGNGLJGJP_pb2.MPMGNGLJGJP, _Mapping]]] = ..., JOILDLJPNEC: _Optional[int] = ..., AHBIDIAELPL: _Optional[int] = ..., LFGCGEDEBGM: _Optional[int] = ..., KEJDLAEBHIF: _Optional[int] = ..., JMGEOCMBEKF: bool = ..., DFANCLIKIOI: bool = ..., PCJNMGGMLJE: _Optional[int] = ...) -> None: ...
