from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassMission(_message.Message):
    __slots__ = ("reward_battle_pass_point", "mission_status", "cur_progress", "total_progress", "mission_id", "mission_type")
    class MissionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MISSION_STATUS_INVALID: _ClassVar[BattlePassMission.MissionStatus]
        MISSION_STATUS_UNFINISHED: _ClassVar[BattlePassMission.MissionStatus]
        MISSION_STATUS_FINISHED: _ClassVar[BattlePassMission.MissionStatus]
        MISSION_STATUS_POINT_TAKEN: _ClassVar[BattlePassMission.MissionStatus]
    MISSION_STATUS_INVALID: BattlePassMission.MissionStatus
    MISSION_STATUS_UNFINISHED: BattlePassMission.MissionStatus
    MISSION_STATUS_FINISHED: BattlePassMission.MissionStatus
    MISSION_STATUS_POINT_TAKEN: BattlePassMission.MissionStatus
    REWARD_BATTLE_PASS_POINT_FIELD_NUMBER: _ClassVar[int]
    MISSION_STATUS_FIELD_NUMBER: _ClassVar[int]
    CUR_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    reward_battle_pass_point: int
    mission_status: BattlePassMission.MissionStatus
    cur_progress: int
    total_progress: int
    mission_id: int
    mission_type: int
    def __init__(self, reward_battle_pass_point: _Optional[int] = ..., mission_status: _Optional[_Union[BattlePassMission.MissionStatus, str]] = ..., cur_progress: _Optional[int] = ..., total_progress: _Optional[int] = ..., mission_id: _Optional[int] = ..., mission_type: _Optional[int] = ...) -> None: ...
