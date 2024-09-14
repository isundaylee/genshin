from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PullRecentChatReq(_message.Message):
    __slots__ = ("begin_sequence", "pull_num")
    BEGIN_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PULL_NUM_FIELD_NUMBER: _ClassVar[int]
    begin_sequence: int
    pull_num: int
    def __init__(self, begin_sequence: _Optional[int] = ..., pull_num: _Optional[int] = ...) -> None: ...
