from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AskAddFriendRsp(_message.Message):
    __slots__ = ("target_uid", "retcode", "param")
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    target_uid: int
    retcode: int
    param: int
    def __init__(self, target_uid: _Optional[int] = ..., retcode: _Optional[int] = ..., param: _Optional[int] = ...) -> None: ...
