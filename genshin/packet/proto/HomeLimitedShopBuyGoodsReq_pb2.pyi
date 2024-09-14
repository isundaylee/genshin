from genshin.packet.proto import HomeLimitedShopGoods_pb2 as _HomeLimitedShopGoods_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeLimitedShopBuyGoodsReq(_message.Message):
    __slots__ = ("goods", "buy_count")
    GOODS_FIELD_NUMBER: _ClassVar[int]
    BUY_COUNT_FIELD_NUMBER: _ClassVar[int]
    goods: _HomeLimitedShopGoods_pb2.HomeLimitedShopGoods
    buy_count: int
    def __init__(self, goods: _Optional[_Union[_HomeLimitedShopGoods_pb2.HomeLimitedShopGoods, _Mapping]] = ..., buy_count: _Optional[int] = ...) -> None: ...
