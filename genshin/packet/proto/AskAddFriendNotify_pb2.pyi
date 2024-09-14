from genshin.packet.proto import FriendBrief_pb2 as _FriendBrief_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AskAddFriendNotify(_message.Message):
    __slots__ = ("target_friend_brief", "target_uid")
    TARGET_FRIEND_BRIEF_FIELD_NUMBER: _ClassVar[int]
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    target_friend_brief: _FriendBrief_pb2.FriendBrief
    target_uid: int
    def __init__(self, target_friend_brief: _Optional[_Union[_FriendBrief_pb2.FriendBrief, _Mapping]] = ..., target_uid: _Optional[int] = ...) -> None: ...
