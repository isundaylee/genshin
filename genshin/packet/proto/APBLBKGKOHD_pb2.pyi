from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import KGLMKABNMMM_pb2 as _KGLMKABNMMM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class APBLBKGKOHD(_message.Message):
    __slots__ = ("LNBOJICAIFE", "OPKGNLDIEHJ", "MMMLFIKMDEN", "DLFDIGNBONK", "ECIFINMNLND", "EJNINFFFKJP")
    LNBOJICAIFE_FIELD_NUMBER: _ClassVar[int]
    OPKGNLDIEHJ_FIELD_NUMBER: _ClassVar[int]
    MMMLFIKMDEN_FIELD_NUMBER: _ClassVar[int]
    DLFDIGNBONK_FIELD_NUMBER: _ClassVar[int]
    ECIFINMNLND_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    LNBOJICAIFE: _containers.RepeatedCompositeFieldContainer[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ]
    OPKGNLDIEHJ: _containers.RepeatedCompositeFieldContainer[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ]
    MMMLFIKMDEN: _containers.RepeatedCompositeFieldContainer[_KGLMKABNMMM_pb2.KGLMKABNMMM]
    DLFDIGNBONK: _containers.RepeatedCompositeFieldContainer[_KGLMKABNMMM_pb2.KGLMKABNMMM]
    ECIFINMNLND: int
    EJNINFFFKJP: int
    def __init__(self, LNBOJICAIFE: _Optional[_Iterable[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]]] = ..., OPKGNLDIEHJ: _Optional[_Iterable[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]]] = ..., MMMLFIKMDEN: _Optional[_Iterable[_Union[_KGLMKABNMMM_pb2.KGLMKABNMMM, _Mapping]]] = ..., DLFDIGNBONK: _Optional[_Iterable[_Union[_KGLMKABNMMM_pb2.KGLMKABNMMM, _Mapping]]] = ..., ECIFINMNLND: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
