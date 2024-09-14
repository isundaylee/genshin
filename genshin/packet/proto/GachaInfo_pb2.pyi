from genshin.packet.proto import GachaUpInfo_pb2 as _GachaUpInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GachaInfo(_message.Message):
    __slots__ = ("end_time", "wish_progress", "ten_cost_item_num", "gacha_preview_prefab_path", "begin_time", "gacha_record_url", "cost_item_num", "schedule_id", "gacha_prob_url", "gacha_type", "gacha_prefab_path", "cost_item_id", "wish_max_progress", "left_gacha_times", "gacha_times_limit", "display_up5_item_list", "ten_cost_item_id", "is_new_wish", "wish_item_id", "title_textmap", "gacha_prob_url_oversea", "cur_schedule_daily_gacha_times", "EFPBICLMCGG", "LAGAHPEKLHM", "gacha_up_info_list", "display_up4_item_list", "gacha_sort_id", "gacha_record_url_oversea")
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    WISH_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TEN_COST_ITEM_NUM_FIELD_NUMBER: _ClassVar[int]
    GACHA_PREVIEW_PREFAB_PATH_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    GACHA_RECORD_URL_FIELD_NUMBER: _ClassVar[int]
    COST_ITEM_NUM_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    GACHA_PROB_URL_FIELD_NUMBER: _ClassVar[int]
    GACHA_TYPE_FIELD_NUMBER: _ClassVar[int]
    GACHA_PREFAB_PATH_FIELD_NUMBER: _ClassVar[int]
    COST_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    WISH_MAX_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    LEFT_GACHA_TIMES_FIELD_NUMBER: _ClassVar[int]
    GACHA_TIMES_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_UP5_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    TEN_COST_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_WISH_FIELD_NUMBER: _ClassVar[int]
    WISH_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_TEXTMAP_FIELD_NUMBER: _ClassVar[int]
    GACHA_PROB_URL_OVERSEA_FIELD_NUMBER: _ClassVar[int]
    CUR_SCHEDULE_DAILY_GACHA_TIMES_FIELD_NUMBER: _ClassVar[int]
    EFPBICLMCGG_FIELD_NUMBER: _ClassVar[int]
    LAGAHPEKLHM_FIELD_NUMBER: _ClassVar[int]
    GACHA_UP_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_UP4_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    GACHA_SORT_ID_FIELD_NUMBER: _ClassVar[int]
    GACHA_RECORD_URL_OVERSEA_FIELD_NUMBER: _ClassVar[int]
    end_time: int
    wish_progress: int
    ten_cost_item_num: int
    gacha_preview_prefab_path: str
    begin_time: int
    gacha_record_url: str
    cost_item_num: int
    schedule_id: int
    gacha_prob_url: str
    gacha_type: int
    gacha_prefab_path: str
    cost_item_id: int
    wish_max_progress: int
    left_gacha_times: int
    gacha_times_limit: int
    display_up5_item_list: _containers.RepeatedScalarFieldContainer[int]
    ten_cost_item_id: int
    is_new_wish: bool
    wish_item_id: int
    title_textmap: str
    gacha_prob_url_oversea: str
    cur_schedule_daily_gacha_times: int
    EFPBICLMCGG: _containers.RepeatedScalarFieldContainer[int]
    LAGAHPEKLHM: bool
    gacha_up_info_list: _containers.RepeatedCompositeFieldContainer[_GachaUpInfo_pb2.GachaUpInfo]
    display_up4_item_list: _containers.RepeatedScalarFieldContainer[int]
    gacha_sort_id: int
    gacha_record_url_oversea: str
    def __init__(self, end_time: _Optional[int] = ..., wish_progress: _Optional[int] = ..., ten_cost_item_num: _Optional[int] = ..., gacha_preview_prefab_path: _Optional[str] = ..., begin_time: _Optional[int] = ..., gacha_record_url: _Optional[str] = ..., cost_item_num: _Optional[int] = ..., schedule_id: _Optional[int] = ..., gacha_prob_url: _Optional[str] = ..., gacha_type: _Optional[int] = ..., gacha_prefab_path: _Optional[str] = ..., cost_item_id: _Optional[int] = ..., wish_max_progress: _Optional[int] = ..., left_gacha_times: _Optional[int] = ..., gacha_times_limit: _Optional[int] = ..., display_up5_item_list: _Optional[_Iterable[int]] = ..., ten_cost_item_id: _Optional[int] = ..., is_new_wish: bool = ..., wish_item_id: _Optional[int] = ..., title_textmap: _Optional[str] = ..., gacha_prob_url_oversea: _Optional[str] = ..., cur_schedule_daily_gacha_times: _Optional[int] = ..., EFPBICLMCGG: _Optional[_Iterable[int]] = ..., LAGAHPEKLHM: bool = ..., gacha_up_info_list: _Optional[_Iterable[_Union[_GachaUpInfo_pb2.GachaUpInfo, _Mapping]]] = ..., display_up4_item_list: _Optional[_Iterable[int]] = ..., gacha_sort_id: _Optional[int] = ..., gacha_record_url_oversea: _Optional[str] = ...) -> None: ...
