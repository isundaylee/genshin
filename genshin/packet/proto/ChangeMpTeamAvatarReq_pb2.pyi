from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeMpTeamAvatarReq(_message.Message):
    __slots__ = ("cur_avatar_guid", "avatar_guid_list")
    CUR_AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    cur_avatar_guid: int
    avatar_guid_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, cur_avatar_guid: _Optional[int] = ..., avatar_guid_list: _Optional[_Iterable[int]] = ...) -> None: ...
