from genshin.packet.proto import FriendBrief_pb2 as _FriendBrief_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPlayerFriendListRsp(_message.Message):
    __slots__ = ("retcode", "friend_list", "ask_friend_list")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    FRIEND_LIST_FIELD_NUMBER: _ClassVar[int]
    ASK_FRIEND_LIST_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    friend_list: _containers.RepeatedCompositeFieldContainer[_FriendBrief_pb2.FriendBrief]
    ask_friend_list: _containers.RepeatedCompositeFieldContainer[_FriendBrief_pb2.FriendBrief]
    def __init__(self, retcode: _Optional[int] = ..., friend_list: _Optional[_Iterable[_Union[_FriendBrief_pb2.FriendBrief, _Mapping]]] = ..., ask_friend_list: _Optional[_Iterable[_Union[_FriendBrief_pb2.FriendBrief, _Mapping]]] = ...) -> None: ...
