from genshin.packet.proto import BattlePassCycle_pb2 as _BattlePassCycle_pb2
from genshin.packet.proto import BattlePassRewardPlanOption_pb2 as _BattlePassRewardPlanOption_pb2
from genshin.packet.proto import BattlePassProduct_pb2 as _BattlePassProduct_pb2
from genshin.packet.proto import BattlePassRewardTag_pb2 as _BattlePassRewardTag_pb2
from genshin.packet.proto import BattlePassUnlockStatus_pb2 as _BattlePassUnlockStatus_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassSchedule(_message.Message):
    __slots__ = ("cur_cycle", "reward_plan_option_list", "product_info", "LOPPMEONNEG", "reward_taken_list", "cur_cycle_points", "begin_time", "is_extra_paid_reward_taken", "end_time", "point", "paid_platform_flags", "schedule_id", "is_viewed", "unlock_status", "level")
    CUR_CYCLE_FIELD_NUMBER: _ClassVar[int]
    REWARD_PLAN_OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_INFO_FIELD_NUMBER: _ClassVar[int]
    LOPPMEONNEG_FIELD_NUMBER: _ClassVar[int]
    REWARD_TAKEN_LIST_FIELD_NUMBER: _ClassVar[int]
    CUR_CYCLE_POINTS_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_EXTRA_PAID_REWARD_TAKEN_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    PAID_PLATFORM_FLAGS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_VIEWED_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_STATUS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    cur_cycle: _BattlePassCycle_pb2.BattlePassCycle
    reward_plan_option_list: _containers.RepeatedCompositeFieldContainer[_BattlePassRewardPlanOption_pb2.BattlePassRewardPlanOption]
    product_info: _BattlePassProduct_pb2.BattlePassProduct
    LOPPMEONNEG: bool
    reward_taken_list: _containers.RepeatedCompositeFieldContainer[_BattlePassRewardTag_pb2.BattlePassRewardTag]
    cur_cycle_points: int
    begin_time: int
    is_extra_paid_reward_taken: bool
    end_time: int
    point: int
    paid_platform_flags: int
    schedule_id: int
    is_viewed: bool
    unlock_status: _BattlePassUnlockStatus_pb2.BattlePassUnlockStatus
    level: int
    def __init__(self, cur_cycle: _Optional[_Union[_BattlePassCycle_pb2.BattlePassCycle, _Mapping]] = ..., reward_plan_option_list: _Optional[_Iterable[_Union[_BattlePassRewardPlanOption_pb2.BattlePassRewardPlanOption, _Mapping]]] = ..., product_info: _Optional[_Union[_BattlePassProduct_pb2.BattlePassProduct, _Mapping]] = ..., LOPPMEONNEG: bool = ..., reward_taken_list: _Optional[_Iterable[_Union[_BattlePassRewardTag_pb2.BattlePassRewardTag, _Mapping]]] = ..., cur_cycle_points: _Optional[int] = ..., begin_time: _Optional[int] = ..., is_extra_paid_reward_taken: bool = ..., end_time: _Optional[int] = ..., point: _Optional[int] = ..., paid_platform_flags: _Optional[int] = ..., schedule_id: _Optional[int] = ..., is_viewed: bool = ..., unlock_status: _Optional[_Union[_BattlePassUnlockStatus_pb2.BattlePassUnlockStatus, str]] = ..., level: _Optional[int] = ...) -> None: ...
