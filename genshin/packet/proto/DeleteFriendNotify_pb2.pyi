from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteFriendNotify(_message.Message):
    __slots__ = ("target_uid",)
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    target_uid: int
    def __init__(self, target_uid: _Optional[int] = ...) -> None: ...
