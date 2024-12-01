from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import NKKHONKPPLE_pb2 as _NKKHONKPPLE_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DEIGILFODBD(_message.Message):
    __slots__ = ("GJEBAJAJPII", "FGFLJIAEMLJ", "level", "KLMDAPCLGAP", "gadget", "monster_id", "gadget_id", "item_id", "npc_id", "IGBDOEBPPHO", "BKHPLMCODAC")
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    FGFLJIAEMLJ_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    KLMDAPCLGAP_FIELD_NUMBER: _ClassVar[int]
    GADGET_FIELD_NUMBER: _ClassVar[int]
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    NPC_ID_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    BKHPLMCODAC_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    FGFLJIAEMLJ: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    level: int
    KLMDAPCLGAP: int
    gadget: _NKKHONKPPLE_pb2.NKKHONKPPLE
    monster_id: int
    gadget_id: int
    item_id: int
    npc_id: int
    IGBDOEBPPHO: int
    BKHPLMCODAC: int
    def __init__(self, GJEBAJAJPII: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., FGFLJIAEMLJ: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., level: _Optional[int] = ..., KLMDAPCLGAP: _Optional[int] = ..., gadget: _Optional[_Union[_NKKHONKPPLE_pb2.NKKHONKPPLE, _Mapping]] = ..., monster_id: _Optional[int] = ..., gadget_id: _Optional[int] = ..., item_id: _Optional[int] = ..., npc_id: _Optional[int] = ..., IGBDOEBPPHO: _Optional[int] = ..., BKHPLMCODAC: _Optional[int] = ...) -> None: ...
