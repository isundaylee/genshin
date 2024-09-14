from genshin.packet.proto import ShopGoods_pb2 as _ShopGoods_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuyGoodsRsp(_message.Message):
    __slots__ = ("goods_list", "retcode", "goods", "buy_count", "shop_type")
    GOODS_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    GOODS_FIELD_NUMBER: _ClassVar[int]
    BUY_COUNT_FIELD_NUMBER: _ClassVar[int]
    SHOP_TYPE_FIELD_NUMBER: _ClassVar[int]
    goods_list: _containers.RepeatedCompositeFieldContainer[_ShopGoods_pb2.ShopGoods]
    retcode: int
    goods: _ShopGoods_pb2.ShopGoods
    buy_count: int
    shop_type: int
    def __init__(self, goods_list: _Optional[_Iterable[_Union[_ShopGoods_pb2.ShopGoods, _Mapping]]] = ..., retcode: _Optional[int] = ..., goods: _Optional[_Union[_ShopGoods_pb2.ShopGoods, _Mapping]] = ..., buy_count: _Optional[int] = ..., shop_type: _Optional[int] = ...) -> None: ...
