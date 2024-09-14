from genshin.packet.proto import ShopMcoinProduct_pb2 as _ShopMcoinProduct_pb2
from genshin.packet.proto import ShopCardProduct_pb2 as _ShopCardProduct_pb2
from genshin.packet.proto import ShopGoods_pb2 as _ShopGoods_pb2
from genshin.packet.proto import ShopConcertProduct_pb2 as _ShopConcertProduct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Shop(_message.Message):
    __slots__ = ("city_reputation_level", "shop_type", "next_refresh_time", "DGEAKOFNGDN", "mcoin_product_list", "card_product_list", "goods_list", "concert_product_list", "city_id")
    CITY_REPUTATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SHOP_TYPE_FIELD_NUMBER: _ClassVar[int]
    NEXT_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    DGEAKOFNGDN_FIELD_NUMBER: _ClassVar[int]
    MCOIN_PRODUCT_LIST_FIELD_NUMBER: _ClassVar[int]
    CARD_PRODUCT_LIST_FIELD_NUMBER: _ClassVar[int]
    GOODS_LIST_FIELD_NUMBER: _ClassVar[int]
    CONCERT_PRODUCT_LIST_FIELD_NUMBER: _ClassVar[int]
    CITY_ID_FIELD_NUMBER: _ClassVar[int]
    city_reputation_level: int
    shop_type: int
    next_refresh_time: int
    DGEAKOFNGDN: int
    mcoin_product_list: _containers.RepeatedCompositeFieldContainer[_ShopMcoinProduct_pb2.ShopMcoinProduct]
    card_product_list: _containers.RepeatedCompositeFieldContainer[_ShopCardProduct_pb2.ShopCardProduct]
    goods_list: _containers.RepeatedCompositeFieldContainer[_ShopGoods_pb2.ShopGoods]
    concert_product_list: _containers.RepeatedCompositeFieldContainer[_ShopConcertProduct_pb2.ShopConcertProduct]
    city_id: int
    def __init__(self, city_reputation_level: _Optional[int] = ..., shop_type: _Optional[int] = ..., next_refresh_time: _Optional[int] = ..., DGEAKOFNGDN: _Optional[int] = ..., mcoin_product_list: _Optional[_Iterable[_Union[_ShopMcoinProduct_pb2.ShopMcoinProduct, _Mapping]]] = ..., card_product_list: _Optional[_Iterable[_Union[_ShopCardProduct_pb2.ShopCardProduct, _Mapping]]] = ..., goods_list: _Optional[_Iterable[_Union[_ShopGoods_pb2.ShopGoods, _Mapping]]] = ..., concert_product_list: _Optional[_Iterable[_Union[_ShopConcertProduct_pb2.ShopConcertProduct, _Mapping]]] = ..., city_id: _Optional[int] = ...) -> None: ...
