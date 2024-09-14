from genshin.packet.proto import StrengthenPointData_pb2 as _StrengthenPointData_pb2
from genshin.packet.proto import ChallengeFinishType_pb2 as _ChallengeFinishType_pb2
from genshin.packet.proto import CustomDungeonResultInfo_pb2 as _CustomDungeonResultInfo_pb2
from genshin.packet.proto import PotionDungeonResultInfo_pb2 as _PotionDungeonResultInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonChallengeFinishNotify(_message.Message):
    __slots__ = ("challenge_index", "strengthen_point_data_map", "is_success", "current_value", "time_cost", "challenge_record_type", "is_new_record", "finish_type", "custom_dungeon_result_info", "potion_dungeon_result_info")
    class StrengthenPointDataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _StrengthenPointData_pb2.StrengthenPointData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_StrengthenPointData_pb2.StrengthenPointData, _Mapping]] = ...) -> None: ...
    CHALLENGE_INDEX_FIELD_NUMBER: _ClassVar[int]
    STRENGTHEN_POINT_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIME_COST_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_RECORD_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_RECORD_FIELD_NUMBER: _ClassVar[int]
    FINISH_TYPE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_DUNGEON_RESULT_INFO_FIELD_NUMBER: _ClassVar[int]
    POTION_DUNGEON_RESULT_INFO_FIELD_NUMBER: _ClassVar[int]
    challenge_index: int
    strengthen_point_data_map: _containers.MessageMap[int, _StrengthenPointData_pb2.StrengthenPointData]
    is_success: bool
    current_value: int
    time_cost: int
    challenge_record_type: int
    is_new_record: bool
    finish_type: _ChallengeFinishType_pb2.ChallengeFinishType
    custom_dungeon_result_info: _CustomDungeonResultInfo_pb2.CustomDungeonResultInfo
    potion_dungeon_result_info: _PotionDungeonResultInfo_pb2.PotionDungeonResultInfo
    def __init__(self, challenge_index: _Optional[int] = ..., strengthen_point_data_map: _Optional[_Mapping[int, _StrengthenPointData_pb2.StrengthenPointData]] = ..., is_success: bool = ..., current_value: _Optional[int] = ..., time_cost: _Optional[int] = ..., challenge_record_type: _Optional[int] = ..., is_new_record: bool = ..., finish_type: _Optional[_Union[_ChallengeFinishType_pb2.ChallengeFinishType, str]] = ..., custom_dungeon_result_info: _Optional[_Union[_CustomDungeonResultInfo_pb2.CustomDungeonResultInfo, _Mapping]] = ..., potion_dungeon_result_info: _Optional[_Union[_PotionDungeonResultInfo_pb2.PotionDungeonResultInfo, _Mapping]] = ...) -> None: ...
