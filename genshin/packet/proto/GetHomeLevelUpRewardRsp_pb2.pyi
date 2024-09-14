from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetHomeLevelUpRewardRsp(_message.Message):
    __slots__ = ("retcode", "level")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    level: int
    def __init__(self, retcode: _Optional[int] = ..., level: _Optional[int] = ...) -> None: ...
