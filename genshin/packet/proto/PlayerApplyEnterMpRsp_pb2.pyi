from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerApplyEnterMpRsp(_message.Message):
    __slots__ = ("param", "retcode", "target_uid")
    PARAM_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    param: int
    retcode: int
    target_uid: int
    def __init__(self, param: _Optional[int] = ..., retcode: _Optional[int] = ..., target_uid: _Optional[int] = ...) -> None: ...
