from genshin.packet.proto import ActivityWatcherInfo_pb2 as _ActivityWatcherInfo_pb2
from genshin.packet.proto import ActivityPushTipsData_pb2 as _ActivityPushTipsData_pb2
from genshin.packet.proto import MusicGameActivityDetailInfo_pb2 as _MusicGameActivityDetailInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityInfo(_message.Message):
    __slots__ = ("meet_cond_list", "end_time", "begin_time", "is_finished", "FALGLCJDKCL", "watcher_info_list", "expire_cond_list", "schedule_id", "ONCLIGBKLPF", "activity_type", "activity_id", "cur_score", "FFGHMFNFPNL", "first_day_start_time", "LKODGHFICBH", "CDBIIEIPBFF", "LCHFFKHPJIO", "ILKPGDKEIEG", "taken_reward_list", "CIDDJFNIMPJ", "activity_push_tips_data_list", "MPPFCLCENAP", "GONEPFEDMEL", "NJCGNGLKPBJ", "ODMJHPBFIKO", "activity_coin_map", "wish_gift_num_map", "music_game_info")
    class ActivityCoinMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class WishGiftNumMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MEET_COND_LIST_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_FINISHED_FIELD_NUMBER: _ClassVar[int]
    FALGLCJDKCL_FIELD_NUMBER: _ClassVar[int]
    WATCHER_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_COND_LIST_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    ONCLIGBKLPF_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    CUR_SCORE_FIELD_NUMBER: _ClassVar[int]
    FFGHMFNFPNL_FIELD_NUMBER: _ClassVar[int]
    FIRST_DAY_START_TIME_FIELD_NUMBER: _ClassVar[int]
    LKODGHFICBH_FIELD_NUMBER: _ClassVar[int]
    CDBIIEIPBFF_FIELD_NUMBER: _ClassVar[int]
    LCHFFKHPJIO_FIELD_NUMBER: _ClassVar[int]
    ILKPGDKEIEG_FIELD_NUMBER: _ClassVar[int]
    TAKEN_REWARD_LIST_FIELD_NUMBER: _ClassVar[int]
    CIDDJFNIMPJ_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_PUSH_TIPS_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    MPPFCLCENAP_FIELD_NUMBER: _ClassVar[int]
    GONEPFEDMEL_FIELD_NUMBER: _ClassVar[int]
    NJCGNGLKPBJ_FIELD_NUMBER: _ClassVar[int]
    ODMJHPBFIKO_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_COIN_MAP_FIELD_NUMBER: _ClassVar[int]
    WISH_GIFT_NUM_MAP_FIELD_NUMBER: _ClassVar[int]
    MUSIC_GAME_INFO_FIELD_NUMBER: _ClassVar[int]
    meet_cond_list: _containers.RepeatedScalarFieldContainer[int]
    end_time: int
    begin_time: int
    is_finished: bool
    FALGLCJDKCL: bool
    watcher_info_list: _containers.RepeatedCompositeFieldContainer[_ActivityWatcherInfo_pb2.ActivityWatcherInfo]
    expire_cond_list: _containers.RepeatedScalarFieldContainer[int]
    schedule_id: int
    ONCLIGBKLPF: bool
    activity_type: int
    activity_id: int
    cur_score: int
    FFGHMFNFPNL: int
    first_day_start_time: int
    LKODGHFICBH: int
    CDBIIEIPBFF: bool
    LCHFFKHPJIO: bool
    ILKPGDKEIEG: bool
    taken_reward_list: _containers.RepeatedScalarFieldContainer[int]
    CIDDJFNIMPJ: int
    activity_push_tips_data_list: _containers.RepeatedCompositeFieldContainer[_ActivityPushTipsData_pb2.ActivityPushTipsData]
    MPPFCLCENAP: int
    GONEPFEDMEL: _containers.RepeatedScalarFieldContainer[int]
    NJCGNGLKPBJ: _containers.RepeatedScalarFieldContainer[int]
    ODMJHPBFIKO: bool
    activity_coin_map: _containers.ScalarMap[int, int]
    wish_gift_num_map: _containers.ScalarMap[int, int]
    music_game_info: _MusicGameActivityDetailInfo_pb2.MusicGameActivityDetailInfo
    def __init__(self, meet_cond_list: _Optional[_Iterable[int]] = ..., end_time: _Optional[int] = ..., begin_time: _Optional[int] = ..., is_finished: bool = ..., FALGLCJDKCL: bool = ..., watcher_info_list: _Optional[_Iterable[_Union[_ActivityWatcherInfo_pb2.ActivityWatcherInfo, _Mapping]]] = ..., expire_cond_list: _Optional[_Iterable[int]] = ..., schedule_id: _Optional[int] = ..., ONCLIGBKLPF: bool = ..., activity_type: _Optional[int] = ..., activity_id: _Optional[int] = ..., cur_score: _Optional[int] = ..., FFGHMFNFPNL: _Optional[int] = ..., first_day_start_time: _Optional[int] = ..., LKODGHFICBH: _Optional[int] = ..., CDBIIEIPBFF: bool = ..., LCHFFKHPJIO: bool = ..., ILKPGDKEIEG: bool = ..., taken_reward_list: _Optional[_Iterable[int]] = ..., CIDDJFNIMPJ: _Optional[int] = ..., activity_push_tips_data_list: _Optional[_Iterable[_Union[_ActivityPushTipsData_pb2.ActivityPushTipsData, _Mapping]]] = ..., MPPFCLCENAP: _Optional[int] = ..., GONEPFEDMEL: _Optional[_Iterable[int]] = ..., NJCGNGLKPBJ: _Optional[_Iterable[int]] = ..., ODMJHPBFIKO: bool = ..., activity_coin_map: _Optional[_Mapping[int, int]] = ..., wish_gift_num_map: _Optional[_Mapping[int, int]] = ..., music_game_info: _Optional[_Union[_MusicGameActivityDetailInfo_pb2.MusicGameActivityDetailInfo, _Mapping]] = ...) -> None: ...
