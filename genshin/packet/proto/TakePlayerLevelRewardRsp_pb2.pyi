from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TakePlayerLevelRewardRsp(_message.Message):
    __slots__ = ("level", "reward_id", "retcode")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    level: int
    reward_id: int
    retcode: int
    def __init__(self, level: _Optional[int] = ..., reward_id: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
