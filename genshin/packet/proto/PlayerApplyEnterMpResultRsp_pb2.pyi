from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerApplyEnterMpResultRsp(_message.Message):
    __slots__ = ("apply_uid", "retcode", "param", "is_agreed")
    APPLY_UID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    IS_AGREED_FIELD_NUMBER: _ClassVar[int]
    apply_uid: int
    retcode: int
    param: int
    is_agreed: bool
    def __init__(self, apply_uid: _Optional[int] = ..., retcode: _Optional[int] = ..., param: _Optional[int] = ..., is_agreed: bool = ...) -> None: ...
