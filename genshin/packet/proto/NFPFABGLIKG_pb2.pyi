from genshin.packet.proto import CEGMHFPBAJJ_pb2 as _CEGMHFPBAJJ_pb2
from genshin.packet.proto import DDGGNMCAGLO_pb2 as _DDGGNMCAGLO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NFPFABGLIKG(_message.Message):
    __slots__ = ("GMLAOAGJCAO", "PEEBJAOIKFC", "KCDBADFPIPD", "NNGFNBCAAPI", "DHOPBDIHGCG", "GGKGGGHHLML", "avatar_list", "EAIPGEMKNPO")
    GMLAOAGJCAO_FIELD_NUMBER: _ClassVar[int]
    PEEBJAOIKFC_FIELD_NUMBER: _ClassVar[int]
    KCDBADFPIPD_FIELD_NUMBER: _ClassVar[int]
    NNGFNBCAAPI_FIELD_NUMBER: _ClassVar[int]
    DHOPBDIHGCG_FIELD_NUMBER: _ClassVar[int]
    GGKGGGHHLML_FIELD_NUMBER: _ClassVar[int]
    AVATAR_LIST_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    GMLAOAGJCAO: _containers.RepeatedCompositeFieldContainer[_CEGMHFPBAJJ_pb2.CEGMHFPBAJJ]
    PEEBJAOIKFC: _containers.RepeatedCompositeFieldContainer[_DDGGNMCAGLO_pb2.DDGGNMCAGLO]
    KCDBADFPIPD: _containers.RepeatedScalarFieldContainer[int]
    NNGFNBCAAPI: _containers.RepeatedCompositeFieldContainer[_CEGMHFPBAJJ_pb2.CEGMHFPBAJJ]
    DHOPBDIHGCG: _containers.RepeatedScalarFieldContainer[int]
    GGKGGGHHLML: _containers.RepeatedScalarFieldContainer[int]
    avatar_list: _containers.RepeatedCompositeFieldContainer[_CEGMHFPBAJJ_pb2.CEGMHFPBAJJ]
    EAIPGEMKNPO: int
    def __init__(self, GMLAOAGJCAO: _Optional[_Iterable[_Union[_CEGMHFPBAJJ_pb2.CEGMHFPBAJJ, _Mapping]]] = ..., PEEBJAOIKFC: _Optional[_Iterable[_Union[_DDGGNMCAGLO_pb2.DDGGNMCAGLO, _Mapping]]] = ..., KCDBADFPIPD: _Optional[_Iterable[int]] = ..., NNGFNBCAAPI: _Optional[_Iterable[_Union[_CEGMHFPBAJJ_pb2.CEGMHFPBAJJ, _Mapping]]] = ..., DHOPBDIHGCG: _Optional[_Iterable[int]] = ..., GGKGGGHHLML: _Optional[_Iterable[int]] = ..., avatar_list: _Optional[_Iterable[_Union[_CEGMHFPBAJJ_pb2.CEGMHFPBAJJ, _Mapping]]] = ..., EAIPGEMKNPO: _Optional[int] = ...) -> None: ...
