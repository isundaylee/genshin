from genshin.packet.proto import BattlePassSchedule_pb2 as _BattlePassSchedule_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassCurScheduleUpdateNotify(_message.Message):
    __slots__ = ("default_reward_type", "is_viewed", "have_cur_schedule", "HNDKICJJANM", "cur_schedule")
    DEFAULT_REWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_VIEWED_FIELD_NUMBER: _ClassVar[int]
    HAVE_CUR_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    HNDKICJJANM_FIELD_NUMBER: _ClassVar[int]
    CUR_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    default_reward_type: int
    is_viewed: bool
    have_cur_schedule: bool
    HNDKICJJANM: bool
    cur_schedule: _BattlePassSchedule_pb2.BattlePassSchedule
    def __init__(self, default_reward_type: _Optional[int] = ..., is_viewed: bool = ..., have_cur_schedule: bool = ..., HNDKICJJANM: bool = ..., cur_schedule: _Optional[_Union[_BattlePassSchedule_pb2.BattlePassSchedule, _Mapping]] = ...) -> None: ...
