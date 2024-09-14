from genshin.packet.proto import StrengthenPointData_pb2 as _StrengthenPointData_pb2
from genshin.packet.proto import ParamList_pb2 as _ParamList_pb2
from genshin.packet.proto import TowerLevelEndNotify_pb2 as _TowerLevelEndNotify_pb2
from genshin.packet.proto import TrialAvatarFirstPassDungeonNotify_pb2 as _TrialAvatarFirstPassDungeonNotify_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonSettleNotify(_message.Message):
    __slots__ = ("strengthen_point_data_map", "is_success", "fail_cond_list", "dungeon_id", "FJHHIKOIHKA", "PDLMKFLEKDL", "settle_show", "create_player_uid", "MHHCOEDMPDP", "tower_level_end_notify", "trial_avatar_first_pass_dungeon_notify")
    class StrengthenPointDataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _StrengthenPointData_pb2.StrengthenPointData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_StrengthenPointData_pb2.StrengthenPointData, _Mapping]] = ...) -> None: ...
    class SettleShowEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _ParamList_pb2.ParamList
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_ParamList_pb2.ParamList, _Mapping]] = ...) -> None: ...
    STRENGTHEN_POINT_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAIL_COND_LIST_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    FJHHIKOIHKA_FIELD_NUMBER: _ClassVar[int]
    PDLMKFLEKDL_FIELD_NUMBER: _ClassVar[int]
    SETTLE_SHOW_FIELD_NUMBER: _ClassVar[int]
    CREATE_PLAYER_UID_FIELD_NUMBER: _ClassVar[int]
    MHHCOEDMPDP_FIELD_NUMBER: _ClassVar[int]
    TOWER_LEVEL_END_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    TRIAL_AVATAR_FIRST_PASS_DUNGEON_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    strengthen_point_data_map: _containers.MessageMap[int, _StrengthenPointData_pb2.StrengthenPointData]
    is_success: bool
    fail_cond_list: _containers.RepeatedScalarFieldContainer[int]
    dungeon_id: int
    FJHHIKOIHKA: int
    PDLMKFLEKDL: int
    settle_show: _containers.MessageMap[int, _ParamList_pb2.ParamList]
    create_player_uid: int
    MHHCOEDMPDP: int
    tower_level_end_notify: _TowerLevelEndNotify_pb2.TowerLevelEndNotify
    trial_avatar_first_pass_dungeon_notify: _TrialAvatarFirstPassDungeonNotify_pb2.TrialAvatarFirstPassDungeonNotify
    def __init__(self, strengthen_point_data_map: _Optional[_Mapping[int, _StrengthenPointData_pb2.StrengthenPointData]] = ..., is_success: bool = ..., fail_cond_list: _Optional[_Iterable[int]] = ..., dungeon_id: _Optional[int] = ..., FJHHIKOIHKA: _Optional[int] = ..., PDLMKFLEKDL: _Optional[int] = ..., settle_show: _Optional[_Mapping[int, _ParamList_pb2.ParamList]] = ..., create_player_uid: _Optional[int] = ..., MHHCOEDMPDP: _Optional[int] = ..., tower_level_end_notify: _Optional[_Union[_TowerLevelEndNotify_pb2.TowerLevelEndNotify, _Mapping]] = ..., trial_avatar_first_pass_dungeon_notify: _Optional[_Union[_TrialAvatarFirstPassDungeonNotify_pb2.TrialAvatarFirstPassDungeonNotify, _Mapping]] = ...) -> None: ...
