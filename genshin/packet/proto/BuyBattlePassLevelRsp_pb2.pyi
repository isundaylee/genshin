from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuyBattlePassLevelRsp(_message.Message):
    __slots__ = ("retcode", "buy_level")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    BUY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    buy_level: int
    def __init__(self, retcode: _Optional[int] = ..., buy_level: _Optional[int] = ...) -> None: ...
