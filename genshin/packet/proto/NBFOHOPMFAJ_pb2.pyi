from genshin.packet.proto import CEGMHFPBAJJ_pb2 as _CEGMHFPBAJJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NBFOHOPMFAJ(_message.Message):
    __slots__ = ("avatar_list", "GMLAOAGJCAO", "DHOPBDIHGCG", "EJNINFFFKJP")
    AVATAR_LIST_FIELD_NUMBER: _ClassVar[int]
    GMLAOAGJCAO_FIELD_NUMBER: _ClassVar[int]
    DHOPBDIHGCG_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    avatar_list: _containers.RepeatedCompositeFieldContainer[_CEGMHFPBAJJ_pb2.CEGMHFPBAJJ]
    GMLAOAGJCAO: _containers.RepeatedCompositeFieldContainer[_CEGMHFPBAJJ_pb2.CEGMHFPBAJJ]
    DHOPBDIHGCG: _containers.RepeatedScalarFieldContainer[int]
    EJNINFFFKJP: int
    def __init__(self, avatar_list: _Optional[_Iterable[_Union[_CEGMHFPBAJJ_pb2.CEGMHFPBAJJ, _Mapping]]] = ..., GMLAOAGJCAO: _Optional[_Iterable[_Union[_CEGMHFPBAJJ_pb2.CEGMHFPBAJJ, _Mapping]]] = ..., DHOPBDIHGCG: _Optional[_Iterable[int]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
