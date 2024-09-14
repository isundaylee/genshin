from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DailyDungeonEntryInfo(_message.Message):
    __slots__ = ("dungeon_entry_config_id", "dungeon_entry_id", "recommend_dungeon_id", "next_refresh_time")
    DUNGEON_ENTRY_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    RECOMMEND_DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    dungeon_entry_config_id: int
    dungeon_entry_id: int
    recommend_dungeon_id: int
    next_refresh_time: int
    def __init__(self, dungeon_entry_config_id: _Optional[int] = ..., dungeon_entry_id: _Optional[int] = ..., recommend_dungeon_id: _Optional[int] = ..., next_refresh_time: _Optional[int] = ...) -> None: ...
