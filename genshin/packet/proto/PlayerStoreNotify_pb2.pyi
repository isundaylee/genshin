from genshin.packet.proto import Item_pb2 as _Item_pb2
from genshin.packet.proto import StoreType_pb2 as _StoreType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerStoreNotify(_message.Message):
    __slots__ = ("item_list", "store_type", "weight_limit")
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    STORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_Item_pb2.Item]
    store_type: _StoreType_pb2.StoreType
    weight_limit: int
    def __init__(self, item_list: _Optional[_Iterable[_Union[_Item_pb2.Item, _Mapping]]] = ..., store_type: _Optional[_Union[_StoreType_pb2.StoreType, str]] = ..., weight_limit: _Optional[int] = ...) -> None: ...
