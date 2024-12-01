from genshin.packet.proto import KNOPPNBPEBM_pb2 as _KNOPPNBPEBM_pb2
from genshin.packet.proto import IJLHHNEFLKK_pb2 as _IJLHHNEFLKK_pb2
from genshin.packet.proto import MKGJGOIAOAP_pb2 as _MKGJGOIAOAP_pb2
from genshin.packet.proto import CNHLJKCJAHB_pb2 as _CNHLJKCJAHB_pb2
from genshin.packet.proto import LJJFJILBNLL_pb2 as _LJJFJILBNLL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AAJPEBEBOHD(_message.Message):
    __slots__ = ("PKAICAIONPM", "FBHDEIBPLDL", "PPOCFIEHJAA", "MAGLLNDNDDL", "ICCHDGKMNLF", "LCEHPFCEJEN", "EJNINFFFKJP")
    PKAICAIONPM_FIELD_NUMBER: _ClassVar[int]
    FBHDEIBPLDL_FIELD_NUMBER: _ClassVar[int]
    PPOCFIEHJAA_FIELD_NUMBER: _ClassVar[int]
    MAGLLNDNDDL_FIELD_NUMBER: _ClassVar[int]
    ICCHDGKMNLF_FIELD_NUMBER: _ClassVar[int]
    LCEHPFCEJEN_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    PKAICAIONPM: _containers.RepeatedCompositeFieldContainer[_KNOPPNBPEBM_pb2.KNOPPNBPEBM]
    FBHDEIBPLDL: _containers.RepeatedCompositeFieldContainer[_IJLHHNEFLKK_pb2.IJLHHNEFLKK]
    PPOCFIEHJAA: _containers.RepeatedCompositeFieldContainer[_MKGJGOIAOAP_pb2.MKGJGOIAOAP]
    MAGLLNDNDDL: _containers.RepeatedCompositeFieldContainer[_CNHLJKCJAHB_pb2.CNHLJKCJAHB]
    ICCHDGKMNLF: _LJJFJILBNLL_pb2.LJJFJILBNLL
    LCEHPFCEJEN: int
    EJNINFFFKJP: int
    def __init__(self, PKAICAIONPM: _Optional[_Iterable[_Union[_KNOPPNBPEBM_pb2.KNOPPNBPEBM, _Mapping]]] = ..., FBHDEIBPLDL: _Optional[_Iterable[_Union[_IJLHHNEFLKK_pb2.IJLHHNEFLKK, _Mapping]]] = ..., PPOCFIEHJAA: _Optional[_Iterable[_Union[_MKGJGOIAOAP_pb2.MKGJGOIAOAP, _Mapping]]] = ..., MAGLLNDNDDL: _Optional[_Iterable[_Union[_CNHLJKCJAHB_pb2.CNHLJKCJAHB, _Mapping]]] = ..., ICCHDGKMNLF: _Optional[_Union[_LJJFJILBNLL_pb2.LJJFJILBNLL, _Mapping]] = ..., LCEHPFCEJEN: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
