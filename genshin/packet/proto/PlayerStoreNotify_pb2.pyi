from genshin.packet.proto import Item_pb2 as _Item_pb2
from genshin.packet.proto import StoreType_pb2 as _StoreType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerStoreNotify(_message.Message):
    __slots__ = ("store_type", "item_list", "weight_limit")
    STORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    store_type: _StoreType_pb2.StoreType
    item_list: _containers.RepeatedCompositeFieldContainer[_Item_pb2.Item]
    weight_limit: int
    def __init__(self, store_type: _Optional[_Union[_StoreType_pb2.StoreType, str]] = ..., item_list: _Optional[_Iterable[_Union[_Item_pb2.Item, _Mapping]]] = ..., weight_limit: _Optional[int] = ...) -> None: ...
