from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CardProductRewardNotify(_message.Message):
    __slots__ = ("product_id", "remain_days", "hcoin")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    REMAIN_DAYS_FIELD_NUMBER: _ClassVar[int]
    HCOIN_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    remain_days: int
    hcoin: int
    def __init__(self, product_id: _Optional[str] = ..., remain_days: _Optional[int] = ..., hcoin: _Optional[int] = ...) -> None: ...
