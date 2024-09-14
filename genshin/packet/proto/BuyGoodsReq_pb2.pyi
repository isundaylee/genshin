from genshin.packet.proto import ShopGoods_pb2 as _ShopGoods_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuyGoodsReq(_message.Message):
    __slots__ = ("buy_count", "shop_type", "goods")
    BUY_COUNT_FIELD_NUMBER: _ClassVar[int]
    SHOP_TYPE_FIELD_NUMBER: _ClassVar[int]
    GOODS_FIELD_NUMBER: _ClassVar[int]
    buy_count: int
    shop_type: int
    goods: _ShopGoods_pb2.ShopGoods
    def __init__(self, buy_count: _Optional[int] = ..., shop_type: _Optional[int] = ..., goods: _Optional[_Union[_ShopGoods_pb2.ShopGoods, _Mapping]] = ...) -> None: ...
