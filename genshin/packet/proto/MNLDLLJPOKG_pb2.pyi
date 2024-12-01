from genshin.packet.proto import AvatarTeam_pb2 as _AvatarTeam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MNLDLLJPOKG(_message.Message):
    __slots__ = ("avatar_team_map", "temp_avatar_guid_list", "PBIOIIFOAPA", "cur_avatar_team_id")
    class AvatarTeamMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _AvatarTeam_pb2.AvatarTeam
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_AvatarTeam_pb2.AvatarTeam, _Mapping]] = ...) -> None: ...
    AVATAR_TEAM_MAP_FIELD_NUMBER: _ClassVar[int]
    TEMP_AVATAR_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    PBIOIIFOAPA_FIELD_NUMBER: _ClassVar[int]
    CUR_AVATAR_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_team_map: _containers.MessageMap[int, _AvatarTeam_pb2.AvatarTeam]
    temp_avatar_guid_list: _containers.RepeatedScalarFieldContainer[int]
    PBIOIIFOAPA: _containers.RepeatedScalarFieldContainer[int]
    cur_avatar_team_id: int
    def __init__(self, avatar_team_map: _Optional[_Mapping[int, _AvatarTeam_pb2.AvatarTeam]] = ..., temp_avatar_guid_list: _Optional[_Iterable[int]] = ..., PBIOIIFOAPA: _Optional[_Iterable[int]] = ..., cur_avatar_team_id: _Optional[int] = ...) -> None: ...
