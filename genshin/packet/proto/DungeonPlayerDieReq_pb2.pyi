from genshin.packet.proto import PlayerDieType_pb2 as _PlayerDieType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonPlayerDieReq(_message.Message):
    __slots__ = ("dungeon_id", "die_type")
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    DIE_TYPE_FIELD_NUMBER: _ClassVar[int]
    dungeon_id: int
    die_type: _PlayerDieType_pb2.PlayerDieType
    def __init__(self, dungeon_id: _Optional[int] = ..., die_type: _Optional[_Union[_PlayerDieType_pb2.PlayerDieType, str]] = ...) -> None: ...
