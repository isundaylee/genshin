from genshin.packet.proto import APHHKPJPMPL_pb2 as _APHHKPJPMPL_pb2
from genshin.packet.proto import OAJDEIOKLFK_pb2 as _OAJDEIOKLFK_pb2
from genshin.packet.proto import EPHJFOFEBDA_pb2 as _EPHJFOFEBDA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BANPAIDEPLM(_message.Message):
    __slots__ = ("LILDONIELDM", "JIIHGLAHMLG", "MPMOPBIBLLB", "AIBCCAMBGDK")
    LILDONIELDM_FIELD_NUMBER: _ClassVar[int]
    JIIHGLAHMLG_FIELD_NUMBER: _ClassVar[int]
    MPMOPBIBLLB_FIELD_NUMBER: _ClassVar[int]
    AIBCCAMBGDK_FIELD_NUMBER: _ClassVar[int]
    LILDONIELDM: _containers.RepeatedCompositeFieldContainer[_APHHKPJPMPL_pb2.APHHKPJPMPL]
    JIIHGLAHMLG: _containers.RepeatedCompositeFieldContainer[_OAJDEIOKLFK_pb2.OAJDEIOKLFK]
    MPMOPBIBLLB: _containers.RepeatedCompositeFieldContainer[_EPHJFOFEBDA_pb2.EPHJFOFEBDA]
    AIBCCAMBGDK: bool
    def __init__(self, LILDONIELDM: _Optional[_Iterable[_Union[_APHHKPJPMPL_pb2.APHHKPJPMPL, _Mapping]]] = ..., JIIHGLAHMLG: _Optional[_Iterable[_Union[_OAJDEIOKLFK_pb2.OAJDEIOKLFK, _Mapping]]] = ..., MPMOPBIBLLB: _Optional[_Iterable[_Union[_EPHJFOFEBDA_pb2.EPHJFOFEBDA, _Mapping]]] = ..., AIBCCAMBGDK: bool = ...) -> None: ...
