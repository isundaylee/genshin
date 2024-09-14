from genshin.packet.proto import ResinCard_pb2 as _ResinCard_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShopCardProduct(_message.Message):
    __slots__ = ("product_id", "price_tier", "mcoin_base", "hcoin_per_day", "days", "remain_reward_days", "card_product_type", "resin_card")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_TIER_FIELD_NUMBER: _ClassVar[int]
    MCOIN_BASE_FIELD_NUMBER: _ClassVar[int]
    HCOIN_PER_DAY_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    REMAIN_REWARD_DAYS_FIELD_NUMBER: _ClassVar[int]
    CARD_PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESIN_CARD_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    price_tier: str
    mcoin_base: int
    hcoin_per_day: int
    days: int
    remain_reward_days: int
    card_product_type: int
    resin_card: _ResinCard_pb2.ResinCard
    def __init__(self, product_id: _Optional[str] = ..., price_tier: _Optional[str] = ..., mcoin_base: _Optional[int] = ..., hcoin_per_day: _Optional[int] = ..., days: _Optional[int] = ..., remain_reward_days: _Optional[int] = ..., card_product_type: _Optional[int] = ..., resin_card: _Optional[_Union[_ResinCard_pb2.ResinCard, _Mapping]] = ...) -> None: ...
