from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeaponUpgradeReq(_message.Message):
    __slots__ = ("item_param_list", "target_weapon_guid", "food_weapon_guid_list")
    ITEM_PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    TARGET_WEAPON_GUID_FIELD_NUMBER: _ClassVar[int]
    FOOD_WEAPON_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    item_param_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    target_weapon_guid: int
    food_weapon_guid_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, item_param_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., target_weapon_guid: _Optional[int] = ..., food_weapon_guid_list: _Optional[_Iterable[int]] = ...) -> None: ...
