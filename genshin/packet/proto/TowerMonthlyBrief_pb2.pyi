from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TowerMonthlyBrief(_message.Message):
    __slots__ = ("tower_schedule_id", "best_level_index", "best_floor_index", "total_star_count")
    TOWER_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    BEST_LEVEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    BEST_FLOOR_INDEX_FIELD_NUMBER: _ClassVar[int]
    TOTAL_STAR_COUNT_FIELD_NUMBER: _ClassVar[int]
    tower_schedule_id: int
    best_level_index: int
    best_floor_index: int
    total_star_count: int
    def __init__(self, tower_schedule_id: _Optional[int] = ..., best_level_index: _Optional[int] = ..., best_floor_index: _Optional[int] = ..., total_star_count: _Optional[int] = ...) -> None: ...
