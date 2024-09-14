from genshin.packet.proto import PlayTeamEntityInfo_pb2 as _PlayTeamEntityInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncScenePlayTeamEntityNotify(_message.Message):
    __slots__ = ("scene_id", "entity_info_list")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    entity_info_list: _containers.RepeatedCompositeFieldContainer[_PlayTeamEntityInfo_pb2.PlayTeamEntityInfo]
    def __init__(self, scene_id: _Optional[int] = ..., entity_info_list: _Optional[_Iterable[_Union[_PlayTeamEntityInfo_pb2.PlayTeamEntityInfo, _Mapping]]] = ...) -> None: ...
