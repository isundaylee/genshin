from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteFriendRsp(_message.Message):
    __slots__ = ("target_uid", "retcode")
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    target_uid: int
    retcode: int
    def __init__(self, target_uid: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
