from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FriendEnterHomeOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FRIEND_ENTER_HOME_OPTION_NEED_CONFIRM: _ClassVar[FriendEnterHomeOption]
    FRIEND_ENTER_HOME_OPTION_REFUSE: _ClassVar[FriendEnterHomeOption]
    FRIEND_ENTER_HOME_OPTION_DIRECT: _ClassVar[FriendEnterHomeOption]
FRIEND_ENTER_HOME_OPTION_NEED_CONFIRM: FriendEnterHomeOption
FRIEND_ENTER_HOME_OPTION_REFUSE: FriendEnterHomeOption
FRIEND_ENTER_HOME_OPTION_DIRECT: FriendEnterHomeOption
