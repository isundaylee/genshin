from genshin.packet.proto import Material_pb2 as _Material_pb2
from genshin.packet.proto import Equip_pb2 as _Equip_pb2
from genshin.packet.proto import Furniture_pb2 as _Furniture_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Item(_message.Message):
    __slots__ = ("item_id", "guid", "material", "equip", "furniture")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_FIELD_NUMBER: _ClassVar[int]
    EQUIP_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    guid: int
    material: _Material_pb2.Material
    equip: _Equip_pb2.Equip
    furniture: _Furniture_pb2.Furniture
    def __init__(self, item_id: _Optional[int] = ..., guid: _Optional[int] = ..., material: _Optional[_Union[_Material_pb2.Material, _Mapping]] = ..., equip: _Optional[_Union[_Equip_pb2.Equip, _Mapping]] = ..., furniture: _Optional[_Union[_Furniture_pb2.Furniture, _Mapping]] = ...) -> None: ...
