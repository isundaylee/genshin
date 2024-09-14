from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DealAddFriendResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEAL_ADD_FRIEND_RESULT_TYPE_REJECT: _ClassVar[DealAddFriendResultType]
    DEAL_ADD_FRIEND_RESULT_TYPE_ACCEPT: _ClassVar[DealAddFriendResultType]
DEAL_ADD_FRIEND_RESULT_TYPE_REJECT: DealAddFriendResultType
DEAL_ADD_FRIEND_RESULT_TYPE_ACCEPT: DealAddFriendResultType
