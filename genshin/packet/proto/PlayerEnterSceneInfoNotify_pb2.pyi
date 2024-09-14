from genshin.packet.proto import TeamEnterSceneInfo_pb2 as _TeamEnterSceneInfo_pb2
from genshin.packet.proto import AvatarEnterSceneInfo_pb2 as _AvatarEnterSceneInfo_pb2
from genshin.packet.proto import MPLevelEntityInfo_pb2 as _MPLevelEntityInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerEnterSceneInfoNotify(_message.Message):
    __slots__ = ("team_enter_info", "avatar_enter_info", "enter_scene_token", "mp_level_entity_info", "cur_avatar_entity_id")
    TEAM_ENTER_INFO_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ENTER_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTER_SCENE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MP_LEVEL_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    CUR_AVATAR_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    team_enter_info: _TeamEnterSceneInfo_pb2.TeamEnterSceneInfo
    avatar_enter_info: _containers.RepeatedCompositeFieldContainer[_AvatarEnterSceneInfo_pb2.AvatarEnterSceneInfo]
    enter_scene_token: int
    mp_level_entity_info: _MPLevelEntityInfo_pb2.MPLevelEntityInfo
    cur_avatar_entity_id: int
    def __init__(self, team_enter_info: _Optional[_Union[_TeamEnterSceneInfo_pb2.TeamEnterSceneInfo, _Mapping]] = ..., avatar_enter_info: _Optional[_Iterable[_Union[_AvatarEnterSceneInfo_pb2.AvatarEnterSceneInfo, _Mapping]]] = ..., enter_scene_token: _Optional[int] = ..., mp_level_entity_info: _Optional[_Union[_MPLevelEntityInfo_pb2.MPLevelEntityInfo, _Mapping]] = ..., cur_avatar_entity_id: _Optional[int] = ...) -> None: ...
