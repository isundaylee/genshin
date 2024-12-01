from genshin.packet.proto import BFFDLDJLHOI_pb2 as _BFFDLDJLHOI_pb2
from genshin.packet.proto import NHNLJIBHPMJ_pb2 as _NHNLJIBHPMJ_pb2
from genshin.packet.proto import KOEDPMFBBNH_pb2 as _KOEDPMFBBNH_pb2
from genshin.packet.proto import HKJEAJEBBKK_pb2 as _HKJEAJEBBKK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HMGBJNNDKEM(_message.Message):
    __slots__ = ("BIPADACDOFI", "GDMMBPJHMCO", "AMOLHEFINEK", "JNIOKOCNMLL", "MCPPEKNBHFK", "OAJOOBGHAGM", "CDBFPFOJBIJ", "IAIDJDLLFLJ", "ACBCEPMACIL", "JFLMAFPHFLJ")
    BIPADACDOFI_FIELD_NUMBER: _ClassVar[int]
    GDMMBPJHMCO_FIELD_NUMBER: _ClassVar[int]
    AMOLHEFINEK_FIELD_NUMBER: _ClassVar[int]
    JNIOKOCNMLL_FIELD_NUMBER: _ClassVar[int]
    MCPPEKNBHFK_FIELD_NUMBER: _ClassVar[int]
    OAJOOBGHAGM_FIELD_NUMBER: _ClassVar[int]
    CDBFPFOJBIJ_FIELD_NUMBER: _ClassVar[int]
    IAIDJDLLFLJ_FIELD_NUMBER: _ClassVar[int]
    ACBCEPMACIL_FIELD_NUMBER: _ClassVar[int]
    JFLMAFPHFLJ_FIELD_NUMBER: _ClassVar[int]
    BIPADACDOFI: _containers.RepeatedScalarFieldContainer[int]
    GDMMBPJHMCO: _BFFDLDJLHOI_pb2.BFFDLDJLHOI
    AMOLHEFINEK: _NHNLJIBHPMJ_pb2.NHNLJIBHPMJ
    JNIOKOCNMLL: _KOEDPMFBBNH_pb2.KOEDPMFBBNH
    MCPPEKNBHFK: int
    OAJOOBGHAGM: int
    CDBFPFOJBIJ: _HKJEAJEBBKK_pb2.HKJEAJEBBKK
    IAIDJDLLFLJ: int
    ACBCEPMACIL: bool
    JFLMAFPHFLJ: int
    def __init__(self, BIPADACDOFI: _Optional[_Iterable[int]] = ..., GDMMBPJHMCO: _Optional[_Union[_BFFDLDJLHOI_pb2.BFFDLDJLHOI, _Mapping]] = ..., AMOLHEFINEK: _Optional[_Union[_NHNLJIBHPMJ_pb2.NHNLJIBHPMJ, _Mapping]] = ..., JNIOKOCNMLL: _Optional[_Union[_KOEDPMFBBNH_pb2.KOEDPMFBBNH, _Mapping]] = ..., MCPPEKNBHFK: _Optional[int] = ..., OAJOOBGHAGM: _Optional[int] = ..., CDBFPFOJBIJ: _Optional[_Union[_HKJEAJEBBKK_pb2.HKJEAJEBBKK, str]] = ..., IAIDJDLLFLJ: _Optional[int] = ..., ACBCEPMACIL: bool = ..., JFLMAFPHFLJ: _Optional[int] = ...) -> None: ...
