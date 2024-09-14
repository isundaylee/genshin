from genshin.packet.proto import HomeAvatarTalkFinishInfo_pb2 as _HomeAvatarTalkFinishInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeAvatarTalkFinishInfoNotify(_message.Message):
    __slots__ = ("avatar_talk_info_list",)
    AVATAR_TALK_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    avatar_talk_info_list: _containers.RepeatedCompositeFieldContainer[_HomeAvatarTalkFinishInfo_pb2.HomeAvatarTalkFinishInfo]
    def __init__(self, avatar_talk_info_list: _Optional[_Iterable[_Union[_HomeAvatarTalkFinishInfo_pb2.HomeAvatarTalkFinishInfo, _Mapping]]] = ...) -> None: ...
