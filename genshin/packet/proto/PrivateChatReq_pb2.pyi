from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PrivateChatReq(_message.Message):
    __slots__ = ("target_uid", "icon", "text")
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    target_uid: int
    icon: int
    text: str
    def __init__(self, target_uid: _Optional[int] = ..., icon: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...
