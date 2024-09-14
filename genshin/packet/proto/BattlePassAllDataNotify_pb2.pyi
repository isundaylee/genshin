from genshin.packet.proto import BattlePassSchedule_pb2 as _BattlePassSchedule_pb2
from genshin.packet.proto import BattlePassMission_pb2 as _BattlePassMission_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassAllDataNotify(_message.Message):
    __slots__ = ("have_cur_schedule", "cur_schedule", "HNDKICJJANM", "is_viewed", "mission_list", "default_reward_type")
    HAVE_CUR_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    CUR_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    HNDKICJJANM_FIELD_NUMBER: _ClassVar[int]
    IS_VIEWED_FIELD_NUMBER: _ClassVar[int]
    MISSION_LIST_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_REWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    have_cur_schedule: bool
    cur_schedule: _BattlePassSchedule_pb2.BattlePassSchedule
    HNDKICJJANM: bool
    is_viewed: bool
    mission_list: _containers.RepeatedCompositeFieldContainer[_BattlePassMission_pb2.BattlePassMission]
    default_reward_type: int
    def __init__(self, have_cur_schedule: bool = ..., cur_schedule: _Optional[_Union[_BattlePassSchedule_pb2.BattlePassSchedule, _Mapping]] = ..., HNDKICJJANM: bool = ..., is_viewed: bool = ..., mission_list: _Optional[_Iterable[_Union[_BattlePassMission_pb2.BattlePassMission, _Mapping]]] = ..., default_reward_type: _Optional[int] = ...) -> None: ...
