from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FriendOnlineState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FRIEND_ONLINE_STATE_DISCONNECT: _ClassVar[FriendOnlineState]
    FRIEND_ONLINE_STATE_ONLINE: _ClassVar[FriendOnlineState]
FRIEND_ONLINE_STATE_DISCONNECT: FriendOnlineState
FRIEND_ONLINE_STATE_ONLINE: FriendOnlineState
