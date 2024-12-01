from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import PNKBKDLOEIJ_pb2 as _PNKBKDLOEIJ_pb2
from genshin.packet.proto import MBLMIOIMCFG_pb2 as _MBLMIOIMCFG_pb2
from genshin.packet.proto import DDOIPMKAOHC_pb2 as _DDOIPMKAOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DBLKCDDFCNF(_message.Message):
    __slots__ = ("MIBDMKIPNFP", "DNAFLMMFFJN", "ANGHAMJLGIH", "PPGKLDFLINO", "FNEFMPALDBE", "LHHGGKIENPC", "ECIFINMNLND", "BJLKIHFOKOF", "ABBCMEJDGFL", "CJBFDOFLMEM", "IGBDOEBPPHO")
    MIBDMKIPNFP_FIELD_NUMBER: _ClassVar[int]
    DNAFLMMFFJN_FIELD_NUMBER: _ClassVar[int]
    ANGHAMJLGIH_FIELD_NUMBER: _ClassVar[int]
    PPGKLDFLINO_FIELD_NUMBER: _ClassVar[int]
    FNEFMPALDBE_FIELD_NUMBER: _ClassVar[int]
    LHHGGKIENPC_FIELD_NUMBER: _ClassVar[int]
    ECIFINMNLND_FIELD_NUMBER: _ClassVar[int]
    BJLKIHFOKOF_FIELD_NUMBER: _ClassVar[int]
    ABBCMEJDGFL_FIELD_NUMBER: _ClassVar[int]
    CJBFDOFLMEM_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    MIBDMKIPNFP: _containers.RepeatedCompositeFieldContainer[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ]
    DNAFLMMFFJN: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    ANGHAMJLGIH: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    PPGKLDFLINO: _containers.RepeatedScalarFieldContainer[int]
    FNEFMPALDBE: _PNKBKDLOEIJ_pb2.PNKBKDLOEIJ
    LHHGGKIENPC: _MBLMIOIMCFG_pb2.MBLMIOIMCFG
    ECIFINMNLND: int
    BJLKIHFOKOF: _DDOIPMKAOHC_pb2.DDOIPMKAOHC
    ABBCMEJDGFL: bool
    CJBFDOFLMEM: int
    IGBDOEBPPHO: int
    def __init__(self, MIBDMKIPNFP: _Optional[_Iterable[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]]] = ..., DNAFLMMFFJN: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., ANGHAMJLGIH: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., PPGKLDFLINO: _Optional[_Iterable[int]] = ..., FNEFMPALDBE: _Optional[_Union[_PNKBKDLOEIJ_pb2.PNKBKDLOEIJ, str]] = ..., LHHGGKIENPC: _Optional[_Union[_MBLMIOIMCFG_pb2.MBLMIOIMCFG, str]] = ..., ECIFINMNLND: _Optional[int] = ..., BJLKIHFOKOF: _Optional[_Union[_DDOIPMKAOHC_pb2.DDOIPMKAOHC, str]] = ..., ABBCMEJDGFL: bool = ..., CJBFDOFLMEM: _Optional[int] = ..., IGBDOEBPPHO: _Optional[int] = ...) -> None: ...
