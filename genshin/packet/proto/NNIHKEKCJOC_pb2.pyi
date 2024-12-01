from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import GLGCIDHMKKA_pb2 as _GLGCIDHMKKA_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NNIHKEKCJOC(_message.Message):
    __slots__ = ("NLJPLCOLKFJ", "GJHMJAFNLOJ", "HCGDIDCAOFF", "NCPECOHFOMB", "LIHAKPPEMKL", "HLEPPMEJPPC")
    NLJPLCOLKFJ_FIELD_NUMBER: _ClassVar[int]
    GJHMJAFNLOJ_FIELD_NUMBER: _ClassVar[int]
    HCGDIDCAOFF_FIELD_NUMBER: _ClassVar[int]
    NCPECOHFOMB_FIELD_NUMBER: _ClassVar[int]
    LIHAKPPEMKL_FIELD_NUMBER: _ClassVar[int]
    HLEPPMEJPPC_FIELD_NUMBER: _ClassVar[int]
    NLJPLCOLKFJ: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    GJHMJAFNLOJ: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    HCGDIDCAOFF: float
    NCPECOHFOMB: _GLGCIDHMKKA_pb2.GLGCIDHMKKA
    LIHAKPPEMKL: float
    HLEPPMEJPPC: int
    def __init__(self, NLJPLCOLKFJ: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., GJHMJAFNLOJ: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., HCGDIDCAOFF: _Optional[float] = ..., NCPECOHFOMB: _Optional[_Union[_GLGCIDHMKKA_pb2.GLGCIDHMKKA, str]] = ..., LIHAKPPEMKL: _Optional[float] = ..., HLEPPMEJPPC: _Optional[int] = ...) -> None: ...
