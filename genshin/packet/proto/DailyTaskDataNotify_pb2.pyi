from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DailyTaskDataNotify(_message.Message):
    __slots__ = ("is_taken_score_reward", "score_reward_id", "finished_num")
    IS_TAKEN_SCORE_REWARD_FIELD_NUMBER: _ClassVar[int]
    SCORE_REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    FINISHED_NUM_FIELD_NUMBER: _ClassVar[int]
    is_taken_score_reward: bool
    score_reward_id: int
    finished_num: int
    def __init__(self, is_taken_score_reward: bool = ..., score_reward_id: _Optional[int] = ..., finished_num: _Optional[int] = ...) -> None: ...
