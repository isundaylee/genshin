from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DailyTaskInfo(_message.Message):
    __slots__ = ("is_finished", "progress", "daily_task_id", "finish_progress", "reward_id")
    IS_FINISHED_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    DAILY_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    FINISH_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    is_finished: bool
    progress: int
    daily_task_id: int
    finish_progress: int
    reward_id: int
    def __init__(self, is_finished: bool = ..., progress: _Optional[int] = ..., daily_task_id: _Optional[int] = ..., finish_progress: _Optional[int] = ..., reward_id: _Optional[int] = ...) -> None: ...
