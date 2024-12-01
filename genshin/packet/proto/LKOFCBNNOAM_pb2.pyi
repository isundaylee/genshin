from genshin.packet.proto import KHJMIKAAFHB_pb2 as _KHJMIKAAFHB_pb2
from genshin.packet.proto import NHNLJIBHPMJ_pb2 as _NHNLJIBHPMJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LKOFCBNNOAM(_message.Message):
    __slots__ = ("PEEBJAOIKFC", "AMOLHEFINEK", "OAJOOBGHAGM", "MCPPEKNBHFK")
    PEEBJAOIKFC_FIELD_NUMBER: _ClassVar[int]
    AMOLHEFINEK_FIELD_NUMBER: _ClassVar[int]
    OAJOOBGHAGM_FIELD_NUMBER: _ClassVar[int]
    MCPPEKNBHFK_FIELD_NUMBER: _ClassVar[int]
    PEEBJAOIKFC: _containers.RepeatedCompositeFieldContainer[_KHJMIKAAFHB_pb2.KHJMIKAAFHB]
    AMOLHEFINEK: _NHNLJIBHPMJ_pb2.NHNLJIBHPMJ
    OAJOOBGHAGM: int
    MCPPEKNBHFK: int
    def __init__(self, PEEBJAOIKFC: _Optional[_Iterable[_Union[_KHJMIKAAFHB_pb2.KHJMIKAAFHB, _Mapping]]] = ..., AMOLHEFINEK: _Optional[_Union[_NHNLJIBHPMJ_pb2.NHNLJIBHPMJ, _Mapping]] = ..., OAJOOBGHAGM: _Optional[int] = ..., MCPPEKNBHFK: _Optional[int] = ...) -> None: ...
