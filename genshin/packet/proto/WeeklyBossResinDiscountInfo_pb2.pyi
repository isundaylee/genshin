from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WeeklyBossResinDiscountInfo(_message.Message):
    __slots__ = ("discount_num", "discount_num_limit", "resin_cost", "original_resin_cost")
    DISCOUNT_NUM_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_NUM_LIMIT_FIELD_NUMBER: _ClassVar[int]
    RESIN_COST_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_RESIN_COST_FIELD_NUMBER: _ClassVar[int]
    discount_num: int
    discount_num_limit: int
    resin_cost: int
    original_resin_cost: int
    def __init__(self, discount_num: _Optional[int] = ..., discount_num_limit: _Optional[int] = ..., resin_cost: _Optional[int] = ..., original_resin_cost: _Optional[int] = ...) -> None: ...
