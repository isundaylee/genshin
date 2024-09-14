from genshin.packet.proto import ShowAvatarInfo_pb2 as _ShowAvatarInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFriendShowAvatarInfoRsp(_message.Message):
    __slots__ = ("retcode", "show_avatar_info_list", "uid")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    SHOW_AVATAR_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    show_avatar_info_list: _containers.RepeatedCompositeFieldContainer[_ShowAvatarInfo_pb2.ShowAvatarInfo]
    uid: int
    def __init__(self, retcode: _Optional[int] = ..., show_avatar_info_list: _Optional[_Iterable[_Union[_ShowAvatarInfo_pb2.ShowAvatarInfo, _Mapping]]] = ..., uid: _Optional[int] = ...) -> None: ...
