from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeKickPlayerRsp(_message.Message):
    __slots__ = ("is_kick_all", "target_uid", "retcode")
    IS_KICK_ALL_FIELD_NUMBER: _ClassVar[int]
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    is_kick_all: bool
    target_uid: int
    retcode: int
    def __init__(self, is_kick_all: bool = ..., target_uid: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
