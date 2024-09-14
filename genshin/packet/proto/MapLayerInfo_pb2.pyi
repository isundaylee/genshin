from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MapLayerInfo(_message.Message):
    __slots__ = ("unlocked_map_layer_group_id_list", "unlocked_map_layer_id_list", "unlocked_map_layer_floor_id_list")
    UNLOCKED_MAP_LAYER_GROUP_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    UNLOCKED_MAP_LAYER_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    UNLOCKED_MAP_LAYER_FLOOR_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    unlocked_map_layer_group_id_list: _containers.RepeatedScalarFieldContainer[int]
    unlocked_map_layer_id_list: _containers.RepeatedScalarFieldContainer[int]
    unlocked_map_layer_floor_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, unlocked_map_layer_group_id_list: _Optional[_Iterable[int]] = ..., unlocked_map_layer_id_list: _Optional[_Iterable[int]] = ..., unlocked_map_layer_floor_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
