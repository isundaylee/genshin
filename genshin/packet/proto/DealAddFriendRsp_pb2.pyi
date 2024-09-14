from genshin.packet.proto import DealAddFriendResultType_pb2 as _DealAddFriendResultType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DealAddFriendRsp(_message.Message):
    __slots__ = ("retcode", "target_uid", "deal_add_friend_result")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    DEAL_ADD_FRIEND_RESULT_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    target_uid: int
    deal_add_friend_result: _DealAddFriendResultType_pb2.DealAddFriendResultType
    def __init__(self, retcode: _Optional[int] = ..., target_uid: _Optional[int] = ..., deal_add_friend_result: _Optional[_Union[_DealAddFriendResultType_pb2.DealAddFriendResultType, str]] = ...) -> None: ...
