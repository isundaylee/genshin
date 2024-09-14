from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityTakeWatcherRewardRsp(_message.Message):
    __slots__ = ("watcher_id", "retcode", "activity_id")
    WATCHER_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    watcher_id: int
    retcode: int
    activity_id: int
    def __init__(self, watcher_id: _Optional[int] = ..., retcode: _Optional[int] = ..., activity_id: _Optional[int] = ...) -> None: ...
