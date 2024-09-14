from genshin.packet.proto import TeamEntityInfo_pb2 as _TeamEntityInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncTeamEntityNotify(_message.Message):
    __slots__ = ("scene_id", "team_entity_info_list")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ENTITY_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    team_entity_info_list: _containers.RepeatedCompositeFieldContainer[_TeamEntityInfo_pb2.TeamEntityInfo]
    def __init__(self, scene_id: _Optional[int] = ..., team_entity_info_list: _Optional[_Iterable[_Union[_TeamEntityInfo_pb2.TeamEntityInfo, _Mapping]]] = ...) -> None: ...
