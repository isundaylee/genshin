from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeLimitedShopGoods(_message.Message):
    __slots__ = ("cost_item_list", "NPBGGAMEDJG", "bought_num", "NODBIKCALJI", "goods_item", "JOMBNPMFHGG")
    COST_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    NPBGGAMEDJG_FIELD_NUMBER: _ClassVar[int]
    BOUGHT_NUM_FIELD_NUMBER: _ClassVar[int]
    NODBIKCALJI_FIELD_NUMBER: _ClassVar[int]
    GOODS_ITEM_FIELD_NUMBER: _ClassVar[int]
    JOMBNPMFHGG_FIELD_NUMBER: _ClassVar[int]
    cost_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    NPBGGAMEDJG: int
    bought_num: int
    NODBIKCALJI: int
    goods_item: _ItemParam_pb2.ItemParam
    JOMBNPMFHGG: int
    def __init__(self, cost_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., NPBGGAMEDJG: _Optional[int] = ..., bought_num: _Optional[int] = ..., NODBIKCALJI: _Optional[int] = ..., goods_item: _Optional[_Union[_ItemParam_pb2.ItemParam, _Mapping]] = ..., JOMBNPMFHGG: _Optional[int] = ...) -> None: ...
