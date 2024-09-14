from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ForgeQueueData(_message.Message):
    __slots__ = ("total_finish_timestamp", "avatar_id", "finish_count", "queueId", "unfinishCount", "next_finish_timestamp", "forge_id")
    TOTAL_FINISH_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    FINISH_COUNT_FIELD_NUMBER: _ClassVar[int]
    QUEUEID_FIELD_NUMBER: _ClassVar[int]
    UNFINISHCOUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_FINISH_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FORGE_ID_FIELD_NUMBER: _ClassVar[int]
    total_finish_timestamp: int
    avatar_id: int
    finish_count: int
    queueId: int
    unfinishCount: int
    next_finish_timestamp: int
    forge_id: int
    def __init__(self, total_finish_timestamp: _Optional[int] = ..., avatar_id: _Optional[int] = ..., finish_count: _Optional[int] = ..., queueId: _Optional[int] = ..., unfinishCount: _Optional[int] = ..., next_finish_timestamp: _Optional[int] = ..., forge_id: _Optional[int] = ...) -> None: ...
