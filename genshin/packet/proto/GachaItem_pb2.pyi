from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from genshin.packet.proto import GachaTransferItem_pb2 as _GachaTransferItem_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GachaItem(_message.Message):
    __slots__ = ("gacha_item", "is_flash_card", "is_gacha_item_new", "token_item_list", "transfer_items")
    GACHA_ITEM_FIELD_NUMBER: _ClassVar[int]
    IS_FLASH_CARD_FIELD_NUMBER: _ClassVar[int]
    IS_GACHA_ITEM_NEW_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_ITEMS_FIELD_NUMBER: _ClassVar[int]
    gacha_item: _ItemParam_pb2.ItemParam
    is_flash_card: bool
    is_gacha_item_new: bool
    token_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    transfer_items: _containers.RepeatedCompositeFieldContainer[_GachaTransferItem_pb2.GachaTransferItem]
    def __init__(self, gacha_item: _Optional[_Union[_ItemParam_pb2.ItemParam, _Mapping]] = ..., is_flash_card: bool = ..., is_gacha_item_new: bool = ..., token_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., transfer_items: _Optional[_Iterable[_Union[_GachaTransferItem_pb2.GachaTransferItem, _Mapping]]] = ...) -> None: ...
