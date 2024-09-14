from genshin.packet.proto import HomeLimitedShopGoods_pb2 as _HomeLimitedShopGoods_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeLimitedShopBuyGoodsRsp(_message.Message):
    __slots__ = ("retcode", "buy_count", "goods", "goods_list")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    BUY_COUNT_FIELD_NUMBER: _ClassVar[int]
    GOODS_FIELD_NUMBER: _ClassVar[int]
    GOODS_LIST_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    buy_count: int
    goods: _HomeLimitedShopGoods_pb2.HomeLimitedShopGoods
    goods_list: _containers.RepeatedCompositeFieldContainer[_HomeLimitedShopGoods_pb2.HomeLimitedShopGoods]
    def __init__(self, retcode: _Optional[int] = ..., buy_count: _Optional[int] = ..., goods: _Optional[_Union[_HomeLimitedShopGoods_pb2.HomeLimitedShopGoods, _Mapping]] = ..., goods_list: _Optional[_Iterable[_Union[_HomeLimitedShopGoods_pb2.HomeLimitedShopGoods, _Mapping]]] = ...) -> None: ...
