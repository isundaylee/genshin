from genshin.packet.proto import AbilityString_pb2 as _AbilityString_pb2
from genshin.packet.proto import PlayerDieType_pb2 as _PlayerDieType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldPlayerDieNotify(_message.Message):
    __slots__ = ("GOEACHAMIAF", "murderer_entity_id", "GKHNLKAADNG", "die_type", "gadget_id", "monster_id")
    GOEACHAMIAF_FIELD_NUMBER: _ClassVar[int]
    MURDERER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    GKHNLKAADNG_FIELD_NUMBER: _ClassVar[int]
    DIE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    GOEACHAMIAF: _AbilityString_pb2.AbilityString
    murderer_entity_id: int
    GKHNLKAADNG: int
    die_type: _PlayerDieType_pb2.PlayerDieType
    gadget_id: int
    monster_id: int
    def __init__(self, GOEACHAMIAF: _Optional[_Union[_AbilityString_pb2.AbilityString, _Mapping]] = ..., murderer_entity_id: _Optional[int] = ..., GKHNLKAADNG: _Optional[int] = ..., die_type: _Optional[_Union[_PlayerDieType_pb2.PlayerDieType, str]] = ..., gadget_id: _Optional[int] = ..., monster_id: _Optional[int] = ...) -> None: ...
