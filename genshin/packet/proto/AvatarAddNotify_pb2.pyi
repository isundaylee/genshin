from genshin.packet.proto import AvatarInfo_pb2 as _AvatarInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarAddNotify(_message.Message):
    __slots__ = ("is_in_team", "avatar")
    IS_IN_TEAM_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    is_in_team: bool
    avatar: _AvatarInfo_pb2.AvatarInfo
    def __init__(self, is_in_team: bool = ..., avatar: _Optional[_Union[_AvatarInfo_pb2.AvatarInfo, _Mapping]] = ...) -> None: ...
