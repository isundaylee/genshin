from genshin.packet.proto import DealAddFriendResultType_pb2 as _DealAddFriendResultType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DealAddFriendReq(_message.Message):
    __slots__ = ("deal_add_friend_result", "target_uid")
    DEAL_ADD_FRIEND_RESULT_FIELD_NUMBER: _ClassVar[int]
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    deal_add_friend_result: _DealAddFriendResultType_pb2.DealAddFriendResultType
    target_uid: int
    def __init__(self, deal_add_friend_result: _Optional[_Union[_DealAddFriendResultType_pb2.DealAddFriendResultType, str]] = ..., target_uid: _Optional[int] = ...) -> None: ...
