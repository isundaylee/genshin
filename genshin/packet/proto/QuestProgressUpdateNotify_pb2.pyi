from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuestProgressUpdateNotify(_message.Message):
    __slots__ = ("fail_progress_list", "finish_progress_list", "quest_id")
    FAIL_PROGRESS_LIST_FIELD_NUMBER: _ClassVar[int]
    FINISH_PROGRESS_LIST_FIELD_NUMBER: _ClassVar[int]
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    fail_progress_list: _containers.RepeatedScalarFieldContainer[int]
    finish_progress_list: _containers.RepeatedScalarFieldContainer[int]
    quest_id: int
    def __init__(self, fail_progress_list: _Optional[_Iterable[int]] = ..., finish_progress_list: _Optional[_Iterable[int]] = ..., quest_id: _Optional[int] = ...) -> None: ...
