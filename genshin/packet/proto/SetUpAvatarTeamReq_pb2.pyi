from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetUpAvatarTeamReq(_message.Message):
    __slots__ = ("avatar_team_guid_list", "cur_avatar_guid", "team_id")
    AVATAR_TEAM_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    CUR_AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_team_guid_list: _containers.RepeatedScalarFieldContainer[int]
    cur_avatar_guid: int
    team_id: int
    def __init__(self, avatar_team_guid_list: _Optional[_Iterable[int]] = ..., cur_avatar_guid: _Optional[int] = ..., team_id: _Optional[int] = ...) -> None: ...
