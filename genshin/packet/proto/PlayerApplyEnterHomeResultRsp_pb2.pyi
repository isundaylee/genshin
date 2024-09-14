from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerApplyEnterHomeResultRsp(_message.Message):
    __slots__ = ("is_agreed", "retcode", "param", "apply_uid")
    IS_AGREED_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    APPLY_UID_FIELD_NUMBER: _ClassVar[int]
    is_agreed: bool
    retcode: int
    param: int
    apply_uid: int
    def __init__(self, is_agreed: bool = ..., retcode: _Optional[int] = ..., param: _Optional[int] = ..., apply_uid: _Optional[int] = ...) -> None: ...
