from genshin.packet.proto import FKNCPOHEPDN_pb2 as _FKNCPOHEPDN_pb2
from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EJPDLPLCAJH(_message.Message):
    __slots__ = ("EPBMKILNPJI", "BJJLCOCOBNM", "OAMHNFFOHLO", "ODPCPOIEOKE", "LOBCPCBBFLL", "MEJMLAHLNBO")
    EPBMKILNPJI_FIELD_NUMBER: _ClassVar[int]
    BJJLCOCOBNM_FIELD_NUMBER: _ClassVar[int]
    OAMHNFFOHLO_FIELD_NUMBER: _ClassVar[int]
    ODPCPOIEOKE_FIELD_NUMBER: _ClassVar[int]
    LOBCPCBBFLL_FIELD_NUMBER: _ClassVar[int]
    MEJMLAHLNBO_FIELD_NUMBER: _ClassVar[int]
    EPBMKILNPJI: _containers.RepeatedScalarFieldContainer[int]
    BJJLCOCOBNM: _containers.RepeatedCompositeFieldContainer[_FKNCPOHEPDN_pb2.FKNCPOHEPDN]
    OAMHNFFOHLO: _containers.RepeatedCompositeFieldContainer[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ]
    ODPCPOIEOKE: bool
    LOBCPCBBFLL: bool
    MEJMLAHLNBO: bool
    def __init__(self, EPBMKILNPJI: _Optional[_Iterable[int]] = ..., BJJLCOCOBNM: _Optional[_Iterable[_Union[_FKNCPOHEPDN_pb2.FKNCPOHEPDN, _Mapping]]] = ..., OAMHNFFOHLO: _Optional[_Iterable[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]]] = ..., ODPCPOIEOKE: bool = ..., LOBCPCBBFLL: bool = ..., MEJMLAHLNBO: bool = ...) -> None: ...
