from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeaponUpgradeRsp(_message.Message):
    __slots__ = ("item_param_list", "cur_level", "old_level", "retcode", "target_weapon_guid")
    ITEM_PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    CUR_LEVEL_FIELD_NUMBER: _ClassVar[int]
    OLD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_WEAPON_GUID_FIELD_NUMBER: _ClassVar[int]
    item_param_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    cur_level: int
    old_level: int
    retcode: int
    target_weapon_guid: int
    def __init__(self, item_param_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., cur_level: _Optional[int] = ..., old_level: _Optional[int] = ..., retcode: _Optional[int] = ..., target_weapon_guid: _Optional[int] = ...) -> None: ...
