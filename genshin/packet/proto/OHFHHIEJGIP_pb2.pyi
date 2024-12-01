from genshin.packet.proto import DFOALMCBPMG_pb2 as _DFOALMCBPMG_pb2
from genshin.packet.proto import DBPNILFGBEM_pb2 as _DBPNILFGBEM_pb2
from genshin.packet.proto import OEBGKDDFDFF_pb2 as _OEBGKDDFDFF_pb2
from genshin.packet.proto import FPHKAOPDEHN_pb2 as _FPHKAOPDEHN_pb2
from genshin.packet.proto import LINCBKJPOLL_pb2 as _LINCBKJPOLL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OHFHHIEJGIP(_message.Message):
    __slots__ = ("OGLBBJDNAHG", "DGFJOAHLAID", "LOJNCMHMNIH", "MAEHIEMMLPE", "ADHIBDAJPNK", "BJFHKEKDAKP", "JAGCAHOJNOD", "KAEKAJNALIF", "BCJNOAEINDA", "EDKLAHFOAKP", "LKOFKODPMGO", "JABGACILLEC", "FBDOBGJGNBF", "level", "DNBEFLJLAMB")
    OGLBBJDNAHG_FIELD_NUMBER: _ClassVar[int]
    DGFJOAHLAID_FIELD_NUMBER: _ClassVar[int]
    LOJNCMHMNIH_FIELD_NUMBER: _ClassVar[int]
    MAEHIEMMLPE_FIELD_NUMBER: _ClassVar[int]
    ADHIBDAJPNK_FIELD_NUMBER: _ClassVar[int]
    BJFHKEKDAKP_FIELD_NUMBER: _ClassVar[int]
    JAGCAHOJNOD_FIELD_NUMBER: _ClassVar[int]
    KAEKAJNALIF_FIELD_NUMBER: _ClassVar[int]
    BCJNOAEINDA_FIELD_NUMBER: _ClassVar[int]
    EDKLAHFOAKP_FIELD_NUMBER: _ClassVar[int]
    LKOFKODPMGO_FIELD_NUMBER: _ClassVar[int]
    JABGACILLEC_FIELD_NUMBER: _ClassVar[int]
    FBDOBGJGNBF_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    OGLBBJDNAHG: _containers.RepeatedCompositeFieldContainer[_DFOALMCBPMG_pb2.DFOALMCBPMG]
    DGFJOAHLAID: _DBPNILFGBEM_pb2.DBPNILFGBEM
    LOJNCMHMNIH: _OEBGKDDFDFF_pb2.OEBGKDDFDFF
    MAEHIEMMLPE: _containers.RepeatedCompositeFieldContainer[_FPHKAOPDEHN_pb2.FPHKAOPDEHN]
    ADHIBDAJPNK: bool
    BJFHKEKDAKP: bool
    JAGCAHOJNOD: bool
    KAEKAJNALIF: int
    BCJNOAEINDA: int
    EDKLAHFOAKP: int
    LKOFKODPMGO: int
    JABGACILLEC: int
    FBDOBGJGNBF: _LINCBKJPOLL_pb2.LINCBKJPOLL
    level: int
    DNBEFLJLAMB: int
    def __init__(self, OGLBBJDNAHG: _Optional[_Iterable[_Union[_DFOALMCBPMG_pb2.DFOALMCBPMG, _Mapping]]] = ..., DGFJOAHLAID: _Optional[_Union[_DBPNILFGBEM_pb2.DBPNILFGBEM, _Mapping]] = ..., LOJNCMHMNIH: _Optional[_Union[_OEBGKDDFDFF_pb2.OEBGKDDFDFF, _Mapping]] = ..., MAEHIEMMLPE: _Optional[_Iterable[_Union[_FPHKAOPDEHN_pb2.FPHKAOPDEHN, _Mapping]]] = ..., ADHIBDAJPNK: bool = ..., BJFHKEKDAKP: bool = ..., JAGCAHOJNOD: bool = ..., KAEKAJNALIF: _Optional[int] = ..., BCJNOAEINDA: _Optional[int] = ..., EDKLAHFOAKP: _Optional[int] = ..., LKOFKODPMGO: _Optional[int] = ..., JABGACILLEC: _Optional[int] = ..., FBDOBGJGNBF: _Optional[_Union[_LINCBKJPOLL_pb2.LINCBKJPOLL, str]] = ..., level: _Optional[int] = ..., DNBEFLJLAMB: _Optional[int] = ...) -> None: ...
