from genshin.packet.proto import HomeAvatarTalkFinishInfo_pb2 as _HomeAvatarTalkFinishInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeAvatarTalkRsp(_message.Message):
    __slots__ = ("retcode", "avatar_talk_info")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_TALK_INFO_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    avatar_talk_info: _HomeAvatarTalkFinishInfo_pb2.HomeAvatarTalkFinishInfo
    def __init__(self, retcode: _Optional[int] = ..., avatar_talk_info: _Optional[_Union[_HomeAvatarTalkFinishInfo_pb2.HomeAvatarTalkFinishInfo, _Mapping]] = ...) -> None: ...
