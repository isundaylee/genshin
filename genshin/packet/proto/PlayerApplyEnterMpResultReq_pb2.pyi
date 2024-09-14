from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerApplyEnterMpResultReq(_message.Message):
    __slots__ = ("apply_uid", "is_agreed")
    APPLY_UID_FIELD_NUMBER: _ClassVar[int]
    IS_AGREED_FIELD_NUMBER: _ClassVar[int]
    apply_uid: int
    is_agreed: bool
    def __init__(self, apply_uid: _Optional[int] = ..., is_agreed: bool = ...) -> None: ...
