from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetFriendShowAvatarInfoReq(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    def __init__(self, uid: _Optional[int] = ...) -> None: ...
