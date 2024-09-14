from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarTeam(_message.Message):
    __slots__ = ("team_name", "avatar_guid_list")
    TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    team_name: str
    avatar_guid_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, team_name: _Optional[str] = ..., avatar_guid_list: _Optional[_Iterable[int]] = ...) -> None: ...
