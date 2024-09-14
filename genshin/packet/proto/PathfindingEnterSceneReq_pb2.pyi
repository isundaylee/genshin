from genshin.packet.proto import ObstacleInfo_pb2 as _ObstacleInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PathfindingEnterSceneReq(_message.Message):
    __slots__ = ("obstacles", "HDFCDNCGBBH", "is_editor", "DKEOBFMAFPK", "scene_id", "version", "CDDPHGDDCCN")
    OBSTACLES_FIELD_NUMBER: _ClassVar[int]
    HDFCDNCGBBH_FIELD_NUMBER: _ClassVar[int]
    IS_EDITOR_FIELD_NUMBER: _ClassVar[int]
    DKEOBFMAFPK_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CDDPHGDDCCN_FIELD_NUMBER: _ClassVar[int]
    obstacles: _containers.RepeatedCompositeFieldContainer[_ObstacleInfo_pb2.ObstacleInfo]
    HDFCDNCGBBH: _containers.RepeatedScalarFieldContainer[int]
    is_editor: bool
    DKEOBFMAFPK: int
    scene_id: int
    version: int
    CDDPHGDDCCN: int
    def __init__(self, obstacles: _Optional[_Iterable[_Union[_ObstacleInfo_pb2.ObstacleInfo, _Mapping]]] = ..., HDFCDNCGBBH: _Optional[_Iterable[int]] = ..., is_editor: bool = ..., DKEOBFMAFPK: _Optional[int] = ..., scene_id: _Optional[int] = ..., version: _Optional[int] = ..., CDDPHGDDCCN: _Optional[int] = ...) -> None: ...
