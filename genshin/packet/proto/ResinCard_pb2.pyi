from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResinCard(_message.Message):
    __slots__ = ("base_item_list", "per_day_item_list")
    BASE_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    PER_DAY_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    base_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    per_day_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    def __init__(self, base_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., per_day_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ...) -> None: ...
