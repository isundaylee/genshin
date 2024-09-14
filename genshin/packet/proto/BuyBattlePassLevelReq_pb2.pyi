from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuyBattlePassLevelReq(_message.Message):
    __slots__ = ("buy_level",)
    BUY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    buy_level: int
    def __init__(self, buy_level: _Optional[int] = ...) -> None: ...
