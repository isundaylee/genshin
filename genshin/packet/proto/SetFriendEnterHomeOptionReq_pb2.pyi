from genshin.packet.proto import FriendEnterHomeOption_pb2 as _FriendEnterHomeOption_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetFriendEnterHomeOptionReq(_message.Message):
    __slots__ = ("option",)
    OPTION_FIELD_NUMBER: _ClassVar[int]
    option: _FriendEnterHomeOption_pb2.FriendEnterHomeOption
    def __init__(self, option: _Optional[_Union[_FriendEnterHomeOption_pb2.FriendEnterHomeOption, str]] = ...) -> None: ...
