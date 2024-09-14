from genshin.packet.proto import StoreType_pb2 as _StoreType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StoreWeightLimitNotify(_message.Message):
    __slots__ = ("weapon_count_limit", "weight_limit", "furniture_count_limit", "material_count_limit", "reliquary_count_limit", "store_type")
    WEAPON_COUNT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_COUNT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_COUNT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    RELIQUARY_COUNT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    STORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    weapon_count_limit: int
    weight_limit: int
    furniture_count_limit: int
    material_count_limit: int
    reliquary_count_limit: int
    store_type: _StoreType_pb2.StoreType
    def __init__(self, weapon_count_limit: _Optional[int] = ..., weight_limit: _Optional[int] = ..., furniture_count_limit: _Optional[int] = ..., material_count_limit: _Optional[int] = ..., reliquary_count_limit: _Optional[int] = ..., store_type: _Optional[_Union[_StoreType_pb2.StoreType, str]] = ...) -> None: ...
