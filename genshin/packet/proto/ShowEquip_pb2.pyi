from genshin.packet.proto import Reliquary_pb2 as _Reliquary_pb2
from genshin.packet.proto import Weapon_pb2 as _Weapon_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShowEquip(_message.Message):
    __slots__ = ("item_id", "reliquary", "weapon")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    RELIQUARY_FIELD_NUMBER: _ClassVar[int]
    WEAPON_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    reliquary: _Reliquary_pb2.Reliquary
    weapon: _Weapon_pb2.Weapon
    def __init__(self, item_id: _Optional[int] = ..., reliquary: _Optional[_Union[_Reliquary_pb2.Reliquary, _Mapping]] = ..., weapon: _Optional[_Union[_Weapon_pb2.Weapon, _Mapping]] = ...) -> None: ...
