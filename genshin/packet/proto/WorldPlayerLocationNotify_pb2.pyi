from genshin.packet.proto import PlayerLocationInfo_pb2 as _PlayerLocationInfo_pb2
from genshin.packet.proto import PlayerWorldLocationInfo_pb2 as _PlayerWorldLocationInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldPlayerLocationNotify(_message.Message):
    __slots__ = ("player_loc_list", "player_world_loc_list")
    PLAYER_LOC_LIST_FIELD_NUMBER: _ClassVar[int]
    PLAYER_WORLD_LOC_LIST_FIELD_NUMBER: _ClassVar[int]
    player_loc_list: _containers.RepeatedCompositeFieldContainer[_PlayerLocationInfo_pb2.PlayerLocationInfo]
    player_world_loc_list: _containers.RepeatedCompositeFieldContainer[_PlayerWorldLocationInfo_pb2.PlayerWorldLocationInfo]
    def __init__(self, player_loc_list: _Optional[_Iterable[_Union[_PlayerLocationInfo_pb2.PlayerLocationInfo, _Mapping]]] = ..., player_world_loc_list: _Optional[_Iterable[_Union[_PlayerWorldLocationInfo_pb2.PlayerWorldLocationInfo, _Mapping]]] = ...) -> None: ...
