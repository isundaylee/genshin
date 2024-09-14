from genshin.packet.proto import SceneWeaponInfo_pb2 as _SceneWeaponInfo_pb2
from genshin.packet.proto import SceneReliquaryInfo_pb2 as _SceneReliquaryInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarEquipChangeNotify(_message.Message):
    __slots__ = ("avatar_guid", "weapon", "equip_guid", "equip_type", "reliquary", "item_id")
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    EQUIP_GUID_FIELD_NUMBER: _ClassVar[int]
    EQUIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    RELIQUARY_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_guid: int
    weapon: _SceneWeaponInfo_pb2.SceneWeaponInfo
    equip_guid: int
    equip_type: int
    reliquary: _SceneReliquaryInfo_pb2.SceneReliquaryInfo
    item_id: int
    def __init__(self, avatar_guid: _Optional[int] = ..., weapon: _Optional[_Union[_SceneWeaponInfo_pb2.SceneWeaponInfo, _Mapping]] = ..., equip_guid: _Optional[int] = ..., equip_type: _Optional[int] = ..., reliquary: _Optional[_Union[_SceneReliquaryInfo_pb2.SceneReliquaryInfo, _Mapping]] = ..., item_id: _Optional[int] = ...) -> None: ...
