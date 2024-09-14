from genshin.packet.proto import WeeklyBossResinDiscountInfo_pb2 as _WeeklyBossResinDiscountInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEntryInfo(_message.Message):
    __slots__ = ("is_passed", "dungeon_id", "weekly_boss_resin_discount_info", "boss_chest_num", "next_refresh_time", "max_boss_chest_num")
    IS_PASSED_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_BOSS_RESIN_DISCOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    BOSS_CHEST_NUM_FIELD_NUMBER: _ClassVar[int]
    NEXT_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_BOSS_CHEST_NUM_FIELD_NUMBER: _ClassVar[int]
    is_passed: bool
    dungeon_id: int
    weekly_boss_resin_discount_info: _WeeklyBossResinDiscountInfo_pb2.WeeklyBossResinDiscountInfo
    boss_chest_num: int
    next_refresh_time: int
    max_boss_chest_num: int
    def __init__(self, is_passed: bool = ..., dungeon_id: _Optional[int] = ..., weekly_boss_resin_discount_info: _Optional[_Union[_WeeklyBossResinDiscountInfo_pb2.WeeklyBossResinDiscountInfo, _Mapping]] = ..., boss_chest_num: _Optional[int] = ..., next_refresh_time: _Optional[int] = ..., max_boss_chest_num: _Optional[int] = ...) -> None: ...
