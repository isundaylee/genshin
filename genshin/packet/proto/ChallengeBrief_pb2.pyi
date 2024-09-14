from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChallengeBrief(_message.Message):
    __slots__ = ("challenge_index", "is_success", "challenge_id", "cur_progress")
    CHALLENGE_INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_ID_FIELD_NUMBER: _ClassVar[int]
    CUR_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    challenge_index: int
    is_success: bool
    challenge_id: int
    cur_progress: int
    def __init__(self, challenge_index: _Optional[int] = ..., is_success: bool = ..., challenge_id: _Optional[int] = ..., cur_progress: _Optional[int] = ...) -> None: ...
