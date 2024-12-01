from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import OCAAMCABKGG_pb2 as _OCAAMCABKGG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JDBKONEMPDD(_message.Message):
    __slots__ = ("BNHEAFCGIJM", "GBANJKINLGK", "OEGJAILDLBK", "GDCOFFHMCFJ", "IGBDOEBPPHO")
    BNHEAFCGIJM_FIELD_NUMBER: _ClassVar[int]
    GBANJKINLGK_FIELD_NUMBER: _ClassVar[int]
    OEGJAILDLBK_FIELD_NUMBER: _ClassVar[int]
    GDCOFFHMCFJ_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    BNHEAFCGIJM: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    GBANJKINLGK: _containers.RepeatedCompositeFieldContainer[_OCAAMCABKGG_pb2.OCAAMCABKGG]
    OEGJAILDLBK: int
    GDCOFFHMCFJ: int
    IGBDOEBPPHO: int
    def __init__(self, BNHEAFCGIJM: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., GBANJKINLGK: _Optional[_Iterable[_Union[_OCAAMCABKGG_pb2.OCAAMCABKGG, _Mapping]]] = ..., OEGJAILDLBK: _Optional[int] = ..., GDCOFFHMCFJ: _Optional[int] = ..., IGBDOEBPPHO: _Optional[int] = ...) -> None: ...
