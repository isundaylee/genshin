from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PullPrivateChatReq(_message.Message):
    __slots__ = ("target_uid", "pull_num", "from_sequence")
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    PULL_NUM_FIELD_NUMBER: _ClassVar[int]
    FROM_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    target_uid: int
    pull_num: int
    from_sequence: int
    def __init__(self, target_uid: _Optional[int] = ..., pull_num: _Optional[int] = ..., from_sequence: _Optional[int] = ...) -> None: ...
