from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReliquaryUpgradeReq(_message.Message):
    __slots__ = ("item_param_list", "food_reliquary_guid_list", "target_reliquary_guid")
    ITEM_PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    FOOD_RELIQUARY_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    TARGET_RELIQUARY_GUID_FIELD_NUMBER: _ClassVar[int]
    item_param_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    food_reliquary_guid_list: _containers.RepeatedScalarFieldContainer[int]
    target_reliquary_guid: int
    def __init__(self, item_param_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., food_reliquary_guid_list: _Optional[_Iterable[int]] = ..., target_reliquary_guid: _Optional[int] = ...) -> None: ...
