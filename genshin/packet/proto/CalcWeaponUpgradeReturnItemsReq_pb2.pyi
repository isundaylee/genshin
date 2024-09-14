from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CalcWeaponUpgradeReturnItemsReq(_message.Message):
    __slots__ = ("target_weapon_guid", "item_param_list", "food_weapon_guid_list")
    TARGET_WEAPON_GUID_FIELD_NUMBER: _ClassVar[int]
    ITEM_PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    FOOD_WEAPON_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    target_weapon_guid: int
    item_param_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    food_weapon_guid_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, target_weapon_guid: _Optional[int] = ..., item_param_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., food_weapon_guid_list: _Optional[_Iterable[int]] = ...) -> None: ...
