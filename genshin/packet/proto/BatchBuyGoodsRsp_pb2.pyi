from genshin.packet.proto import BuyGoodsParam_pb2 as _BuyGoodsParam_pb2
from genshin.packet.proto import ShopGoods_pb2 as _ShopGoods_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchBuyGoodsRsp(_message.Message):
    __slots__ = ("goods_list", "buy_goods_list", "retcode", "shop_type")
    GOODS_LIST_FIELD_NUMBER: _ClassVar[int]
    BUY_GOODS_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    SHOP_TYPE_FIELD_NUMBER: _ClassVar[int]
    goods_list: _containers.RepeatedCompositeFieldContainer[_ShopGoods_pb2.ShopGoods]
    buy_goods_list: _containers.RepeatedCompositeFieldContainer[_BuyGoodsParam_pb2.BuyGoodsParam]
    retcode: int
    shop_type: int
    def __init__(self, goods_list: _Optional[_Iterable[_Union[_ShopGoods_pb2.ShopGoods, _Mapping]]] = ..., buy_goods_list: _Optional[_Iterable[_Union[_BuyGoodsParam_pb2.BuyGoodsParam, _Mapping]]] = ..., retcode: _Optional[int] = ..., shop_type: _Optional[int] = ...) -> None: ...
