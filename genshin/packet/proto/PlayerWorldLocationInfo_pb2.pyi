from genshin.packet.proto import PlayerLocationInfo_pb2 as _PlayerLocationInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerWorldLocationInfo(_message.Message):
    __slots__ = ("scene_id", "player_loc")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LOC_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    player_loc: _PlayerLocationInfo_pb2.PlayerLocationInfo
    def __init__(self, scene_id: _Optional[int] = ..., player_loc: _Optional[_Union[_PlayerLocationInfo_pb2.PlayerLocationInfo, _Mapping]] = ...) -> None: ...
