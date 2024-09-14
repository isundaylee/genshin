from genshin.packet.proto import TowerCurLevelRecord_pb2 as _TowerCurLevelRecord_pb2
from genshin.packet.proto import TowerFloorRecord_pb2 as _TowerFloorRecord_pb2
from genshin.packet.proto import TowerMonthlyBrief_pb2 as _TowerMonthlyBrief_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TowerAllDataRsp(_message.Message):
    __slots__ = ("tower_schedule_id", "is_finished_entrance_floor", "valid_floor_record_list", "cur_level_record", "retcode", "skip_floor_granted_reward_item_map", "is_first_interact", "floor_open_time_map", "next_schedule_change_time", "monthly_brief", "tower_floor_record_list", "schedule_start_time", "last_schedule_monthly_brief")
    class SkipFloorGrantedRewardItemMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class FloorOpenTimeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    TOWER_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FINISHED_ENTRANCE_FLOOR_FIELD_NUMBER: _ClassVar[int]
    VALID_FLOOR_RECORD_LIST_FIELD_NUMBER: _ClassVar[int]
    CUR_LEVEL_RECORD_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    SKIP_FLOOR_GRANTED_REWARD_ITEM_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_FIRST_INTERACT_FIELD_NUMBER: _ClassVar[int]
    FLOOR_OPEN_TIME_MAP_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCHEDULE_CHANGE_TIME_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_BRIEF_FIELD_NUMBER: _ClassVar[int]
    TOWER_FLOOR_RECORD_LIST_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_SCHEDULE_MONTHLY_BRIEF_FIELD_NUMBER: _ClassVar[int]
    tower_schedule_id: int
    is_finished_entrance_floor: bool
    valid_floor_record_list: int
    cur_level_record: _TowerCurLevelRecord_pb2.TowerCurLevelRecord
    retcode: int
    skip_floor_granted_reward_item_map: _containers.ScalarMap[int, int]
    is_first_interact: bool
    floor_open_time_map: _containers.ScalarMap[int, int]
    next_schedule_change_time: int
    monthly_brief: _TowerMonthlyBrief_pb2.TowerMonthlyBrief
    tower_floor_record_list: _containers.RepeatedCompositeFieldContainer[_TowerFloorRecord_pb2.TowerFloorRecord]
    schedule_start_time: int
    last_schedule_monthly_brief: _TowerMonthlyBrief_pb2.TowerMonthlyBrief
    def __init__(self, tower_schedule_id: _Optional[int] = ..., is_finished_entrance_floor: bool = ..., valid_floor_record_list: _Optional[int] = ..., cur_level_record: _Optional[_Union[_TowerCurLevelRecord_pb2.TowerCurLevelRecord, _Mapping]] = ..., retcode: _Optional[int] = ..., skip_floor_granted_reward_item_map: _Optional[_Mapping[int, int]] = ..., is_first_interact: bool = ..., floor_open_time_map: _Optional[_Mapping[int, int]] = ..., next_schedule_change_time: _Optional[int] = ..., monthly_brief: _Optional[_Union[_TowerMonthlyBrief_pb2.TowerMonthlyBrief, _Mapping]] = ..., tower_floor_record_list: _Optional[_Iterable[_Union[_TowerFloorRecord_pb2.TowerFloorRecord, _Mapping]]] = ..., schedule_start_time: _Optional[int] = ..., last_schedule_monthly_brief: _Optional[_Union[_TowerMonthlyBrief_pb2.TowerMonthlyBrief, _Mapping]] = ...) -> None: ...
