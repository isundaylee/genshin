from genshin.packet.proto import SceneTeamAvatar_pb2 as _SceneTeamAvatar_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneTeamUpdateNotify(_message.Message):
    __slots__ = ("scene_team_avatar_list", "is_in_mp")
    SCENE_TEAM_AVATAR_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_IN_MP_FIELD_NUMBER: _ClassVar[int]
    scene_team_avatar_list: _containers.RepeatedCompositeFieldContainer[_SceneTeamAvatar_pb2.SceneTeamAvatar]
    is_in_mp: bool
    def __init__(self, scene_team_avatar_list: _Optional[_Iterable[_Union[_SceneTeamAvatar_pb2.SceneTeamAvatar, _Mapping]]] = ..., is_in_mp: bool = ...) -> None: ...