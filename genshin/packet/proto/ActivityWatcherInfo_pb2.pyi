from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityWatcherInfo(_message.Message):
    __slots__ = ("total_progress", "cur_progress", "is_taken_reward", "watcher_id")
    TOTAL_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CUR_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    IS_TAKEN_REWARD_FIELD_NUMBER: _ClassVar[int]
    WATCHER_ID_FIELD_NUMBER: _ClassVar[int]
    total_progress: int
    cur_progress: int
    is_taken_reward: bool
    watcher_id: int
    def __init__(self, total_progress: _Optional[int] = ..., cur_progress: _Optional[int] = ..., is_taken_reward: bool = ..., watcher_id: _Optional[int] = ...) -> None: ...
