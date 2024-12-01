from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import ANBHHDKCDEN_pb2 as _ANBHHDKCDEN_pb2
from genshin.packet.proto import JMDIPFDJIAI_pb2 as _JMDIPFDJIAI_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ECKACOBPKBL(_message.Message):
    __slots__ = ("GJEBAJAJPII", "suite_data", "npc_data", "PCFIAAJEOIJ", "OEGJAILDLBK", "guid")
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    SUITE_DATA_FIELD_NUMBER: _ClassVar[int]
    NPC_DATA_FIELD_NUMBER: _ClassVar[int]
    PCFIAAJEOIJ_FIELD_NUMBER: _ClassVar[int]
    OEGJAILDLBK_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    suite_data: _ANBHHDKCDEN_pb2.ANBHHDKCDEN
    npc_data: _JMDIPFDJIAI_pb2.JMDIPFDJIAI
    PCFIAAJEOIJ: int
    OEGJAILDLBK: int
    guid: int
    def __init__(self, GJEBAJAJPII: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., suite_data: _Optional[_Union[_ANBHHDKCDEN_pb2.ANBHHDKCDEN, _Mapping]] = ..., npc_data: _Optional[_Union[_JMDIPFDJIAI_pb2.JMDIPFDJIAI, _Mapping]] = ..., PCFIAAJEOIJ: _Optional[int] = ..., OEGJAILDLBK: _Optional[int] = ..., guid: _Optional[int] = ...) -> None: ...
