from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetUpAvatarTeamRsp(_message.Message):
    __slots__ = ("cur_avatar_guid", "team_id", "avatar_team_guid_list", "retcode")
    CUR_AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_TEAM_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    cur_avatar_guid: int
    team_id: int
    avatar_team_guid_list: _containers.RepeatedScalarFieldContainer[int]
    retcode: int
    def __init__(self, cur_avatar_guid: _Optional[int] = ..., team_id: _Optional[int] = ..., avatar_team_guid_list: _Optional[_Iterable[int]] = ..., retcode: _Optional[int] = ...) -> None: ...
