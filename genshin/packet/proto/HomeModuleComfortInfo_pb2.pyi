from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeModuleComfortInfo(_message.Message):
    __slots__ = ("world_scene_block_comfort_value_list", "room_scene_comfort_value", "module_id")
    WORLD_SCENE_BLOCK_COMFORT_VALUE_LIST_FIELD_NUMBER: _ClassVar[int]
    ROOM_SCENE_COMFORT_VALUE_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    world_scene_block_comfort_value_list: _containers.RepeatedScalarFieldContainer[int]
    room_scene_comfort_value: int
    module_id: int
    def __init__(self, world_scene_block_comfort_value_list: _Optional[_Iterable[int]] = ..., room_scene_comfort_value: _Optional[int] = ..., module_id: _Optional[int] = ...) -> None: ...
