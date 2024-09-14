from genshin.packet.proto import PlayerLocationInfo_pb2 as _PlayerLocationInfo_pb2
from genshin.packet.proto import VehicleLocationInfo_pb2 as _VehicleLocationInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScenePlayerLocationNotify(_message.Message):
    __slots__ = ("player_loc_list", "scene_id", "vehicle_loc_list")
    PLAYER_LOC_LIST_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_LOC_LIST_FIELD_NUMBER: _ClassVar[int]
    player_loc_list: _containers.RepeatedCompositeFieldContainer[_PlayerLocationInfo_pb2.PlayerLocationInfo]
    scene_id: int
    vehicle_loc_list: _containers.RepeatedCompositeFieldContainer[_VehicleLocationInfo_pb2.VehicleLocationInfo]
    def __init__(self, player_loc_list: _Optional[_Iterable[_Union[_PlayerLocationInfo_pb2.PlayerLocationInfo, _Mapping]]] = ..., scene_id: _Optional[int] = ..., vehicle_loc_list: _Optional[_Iterable[_Union[_VehicleLocationInfo_pb2.VehicleLocationInfo, _Mapping]]] = ...) -> None: ...
