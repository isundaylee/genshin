from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ShopConcertProduct(_message.Message):
    __slots__ = ("product_id", "price_tier", "obtain_count", "obtain_limit", "begin_time", "end_time", "buy_times")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_TIER_FIELD_NUMBER: _ClassVar[int]
    OBTAIN_COUNT_FIELD_NUMBER: _ClassVar[int]
    OBTAIN_LIMIT_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    BUY_TIMES_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    price_tier: str
    obtain_count: int
    obtain_limit: int
    begin_time: int
    end_time: int
    buy_times: int
    def __init__(self, product_id: _Optional[str] = ..., price_tier: _Optional[str] = ..., obtain_count: _Optional[int] = ..., obtain_limit: _Optional[int] = ..., begin_time: _Optional[int] = ..., end_time: _Optional[int] = ..., buy_times: _Optional[int] = ...) -> None: ...
