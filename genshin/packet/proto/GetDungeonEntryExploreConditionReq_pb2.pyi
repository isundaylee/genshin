from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetDungeonEntryExploreConditionReq(_message.Message):
    __slots__ = ("dungeon_entry_config_id", "scene_id", "dungeon_entry_scene_point_id")
    DUNGEON_ENTRY_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_ENTRY_SCENE_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    dungeon_entry_config_id: int
    scene_id: int
    dungeon_entry_scene_point_id: int
    def __init__(self, dungeon_entry_config_id: _Optional[int] = ..., scene_id: _Optional[int] = ..., dungeon_entry_scene_point_id: _Optional[int] = ...) -> None: ...
