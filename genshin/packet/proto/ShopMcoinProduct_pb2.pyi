from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ShopMcoinProduct(_message.Message):
    __slots__ = ("product_id", "price_tier", "mcoin_base", "mcoin_non_first", "mcoin_first", "bought_num", "is_audit")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_TIER_FIELD_NUMBER: _ClassVar[int]
    MCOIN_BASE_FIELD_NUMBER: _ClassVar[int]
    MCOIN_NON_FIRST_FIELD_NUMBER: _ClassVar[int]
    MCOIN_FIRST_FIELD_NUMBER: _ClassVar[int]
    BOUGHT_NUM_FIELD_NUMBER: _ClassVar[int]
    IS_AUDIT_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    price_tier: str
    mcoin_base: int
    mcoin_non_first: int
    mcoin_first: int
    bought_num: int
    is_audit: bool
    def __init__(self, product_id: _Optional[str] = ..., price_tier: _Optional[str] = ..., mcoin_base: _Optional[int] = ..., mcoin_non_first: _Optional[int] = ..., mcoin_first: _Optional[int] = ..., bought_num: _Optional[int] = ..., is_audit: bool = ...) -> None: ...
