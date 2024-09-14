from genshin.packet.proto import ObstacleInfo_pb2 as _ObstacleInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObstacleModifyNotify(_message.Message):
    __slots__ = ("add_obstacles", "PBGEEKLDIKE", "remove_obstacle_ids", "EHFGKOLBOMK", "scene_id")
    ADD_OBSTACLES_FIELD_NUMBER: _ClassVar[int]
    PBGEEKLDIKE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_OBSTACLE_IDS_FIELD_NUMBER: _ClassVar[int]
    EHFGKOLBOMK_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    add_obstacles: _containers.RepeatedCompositeFieldContainer[_ObstacleInfo_pb2.ObstacleInfo]
    PBGEEKLDIKE: _containers.RepeatedScalarFieldContainer[int]
    remove_obstacle_ids: _containers.RepeatedScalarFieldContainer[int]
    EHFGKOLBOMK: _containers.RepeatedScalarFieldContainer[int]
    scene_id: int
    def __init__(self, add_obstacles: _Optional[_Iterable[_Union[_ObstacleInfo_pb2.ObstacleInfo, _Mapping]]] = ..., PBGEEKLDIKE: _Optional[_Iterable[int]] = ..., remove_obstacle_ids: _Optional[_Iterable[int]] = ..., EHFGKOLBOMK: _Optional[_Iterable[int]] = ..., scene_id: _Optional[int] = ...) -> None: ...
