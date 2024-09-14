from genshin.packet.proto import BuyGoodsParam_pb2 as _BuyGoodsParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchBuyGoodsReq(_message.Message):
    __slots__ = ("shop_type", "buy_goods_list")
    SHOP_TYPE_FIELD_NUMBER: _ClassVar[int]
    BUY_GOODS_LIST_FIELD_NUMBER: _ClassVar[int]
    shop_type: int
    buy_goods_list: _containers.RepeatedCompositeFieldContainer[_BuyGoodsParam_pb2.BuyGoodsParam]
    def __init__(self, shop_type: _Optional[int] = ..., buy_goods_list: _Optional[_Iterable[_Union[_BuyGoodsParam_pb2.BuyGoodsParam, _Mapping]]] = ...) -> None: ...
