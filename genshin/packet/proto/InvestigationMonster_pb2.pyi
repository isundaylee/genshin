from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import LockState_pb2 as _LockState_pb2
from genshin.packet.proto import WeeklyBossResinDiscountInfo_pb2 as _WeeklyBossResinDiscountInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvestigationMonster(_message.Message):
    __slots__ = ("id", "is_alive", "boss_chest_num", "resin", "is_area_locked", "max_boss_chest_num", "next_refresh_time", "city_id", "next_boss_chest_refresh_time", "scene_id", "pos", "refresh_interval", "lock_state", "weekly_boss_resin_discount_info", "level", "IDNKJEEDOGC", "monster_id", "group_id", "AGIENJJKPBE")
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ALIVE_FIELD_NUMBER: _ClassVar[int]
    BOSS_CHEST_NUM_FIELD_NUMBER: _ClassVar[int]
    RESIN_FIELD_NUMBER: _ClassVar[int]
    IS_AREA_LOCKED_FIELD_NUMBER: _ClassVar[int]
    MAX_BOSS_CHEST_NUM_FIELD_NUMBER: _ClassVar[int]
    NEXT_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    CITY_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_BOSS_CHEST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    LOCK_STATE_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_BOSS_RESIN_DISCOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    IDNKJEEDOGC_FIELD_NUMBER: _ClassVar[int]
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    AGIENJJKPBE_FIELD_NUMBER: _ClassVar[int]
    id: int
    is_alive: bool
    boss_chest_num: int
    resin: int
    is_area_locked: bool
    max_boss_chest_num: int
    next_refresh_time: int
    city_id: int
    next_boss_chest_refresh_time: int
    scene_id: int
    pos: _Vector_pb2.Vector
    refresh_interval: int
    lock_state: _LockState_pb2.LockState
    weekly_boss_resin_discount_info: _WeeklyBossResinDiscountInfo_pb2.WeeklyBossResinDiscountInfo
    level: int
    IDNKJEEDOGC: bool
    monster_id: int
    group_id: int
    AGIENJJKPBE: int
    def __init__(self, id: _Optional[int] = ..., is_alive: bool = ..., boss_chest_num: _Optional[int] = ..., resin: _Optional[int] = ..., is_area_locked: bool = ..., max_boss_chest_num: _Optional[int] = ..., next_refresh_time: _Optional[int] = ..., city_id: _Optional[int] = ..., next_boss_chest_refresh_time: _Optional[int] = ..., scene_id: _Optional[int] = ..., pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., refresh_interval: _Optional[int] = ..., lock_state: _Optional[_Union[_LockState_pb2.LockState, str]] = ..., weekly_boss_resin_discount_info: _Optional[_Union[_WeeklyBossResinDiscountInfo_pb2.WeeklyBossResinDiscountInfo, _Mapping]] = ..., level: _Optional[int] = ..., IDNKJEEDOGC: bool = ..., monster_id: _Optional[int] = ..., group_id: _Optional[int] = ..., AGIENJJKPBE: _Optional[int] = ...) -> None: ...
