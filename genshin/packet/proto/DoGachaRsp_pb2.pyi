from genshin.packet.proto import GachaItem_pb2 as _GachaItem_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DoGachaRsp(_message.Message):
    __slots__ = ("wish_item_id", "retcode", "gacha_schedule_id", "ten_cost_item_num", "cost_item_id", "left_gacha_times", "gacha_times_limit", "ten_cost_item_id", "gacha_sort_id", "gacha_item_list", "gacha_times", "cost_item_num", "wish_progress", "gacha_type", "wish_max_progress", "new_gacha_random", "cur_schedule_daily_gacha_times", "DBNKDMFDCNG", "is_under_minors_restrict", "daily_gacha_times", "is_under_general_restrict")
    WISH_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    GACHA_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    TEN_COST_ITEM_NUM_FIELD_NUMBER: _ClassVar[int]
    COST_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    LEFT_GACHA_TIMES_FIELD_NUMBER: _ClassVar[int]
    GACHA_TIMES_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TEN_COST_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    GACHA_SORT_ID_FIELD_NUMBER: _ClassVar[int]
    GACHA_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    GACHA_TIMES_FIELD_NUMBER: _ClassVar[int]
    COST_ITEM_NUM_FIELD_NUMBER: _ClassVar[int]
    WISH_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    GACHA_TYPE_FIELD_NUMBER: _ClassVar[int]
    WISH_MAX_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    NEW_GACHA_RANDOM_FIELD_NUMBER: _ClassVar[int]
    CUR_SCHEDULE_DAILY_GACHA_TIMES_FIELD_NUMBER: _ClassVar[int]
    DBNKDMFDCNG_FIELD_NUMBER: _ClassVar[int]
    IS_UNDER_MINORS_RESTRICT_FIELD_NUMBER: _ClassVar[int]
    DAILY_GACHA_TIMES_FIELD_NUMBER: _ClassVar[int]
    IS_UNDER_GENERAL_RESTRICT_FIELD_NUMBER: _ClassVar[int]
    wish_item_id: int
    retcode: int
    gacha_schedule_id: int
    ten_cost_item_num: int
    cost_item_id: int
    left_gacha_times: int
    gacha_times_limit: int
    ten_cost_item_id: int
    gacha_sort_id: int
    gacha_item_list: _containers.RepeatedCompositeFieldContainer[_GachaItem_pb2.GachaItem]
    gacha_times: int
    cost_item_num: int
    wish_progress: int
    gacha_type: int
    wish_max_progress: int
    new_gacha_random: int
    cur_schedule_daily_gacha_times: int
    DBNKDMFDCNG: bool
    is_under_minors_restrict: bool
    daily_gacha_times: int
    is_under_general_restrict: bool
    def __init__(self, wish_item_id: _Optional[int] = ..., retcode: _Optional[int] = ..., gacha_schedule_id: _Optional[int] = ..., ten_cost_item_num: _Optional[int] = ..., cost_item_id: _Optional[int] = ..., left_gacha_times: _Optional[int] = ..., gacha_times_limit: _Optional[int] = ..., ten_cost_item_id: _Optional[int] = ..., gacha_sort_id: _Optional[int] = ..., gacha_item_list: _Optional[_Iterable[_Union[_GachaItem_pb2.GachaItem, _Mapping]]] = ..., gacha_times: _Optional[int] = ..., cost_item_num: _Optional[int] = ..., wish_progress: _Optional[int] = ..., gacha_type: _Optional[int] = ..., wish_max_progress: _Optional[int] = ..., new_gacha_random: _Optional[int] = ..., cur_schedule_daily_gacha_times: _Optional[int] = ..., DBNKDMFDCNG: bool = ..., is_under_minors_restrict: bool = ..., daily_gacha_times: _Optional[int] = ..., is_under_general_restrict: bool = ...) -> None: ...
