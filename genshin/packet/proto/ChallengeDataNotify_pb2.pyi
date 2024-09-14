from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChallengeDataNotify(_message.Message):
    __slots__ = ("value", "param_index", "challenge_index")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PARAM_INDEX_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_INDEX_FIELD_NUMBER: _ClassVar[int]
    value: int
    param_index: int
    challenge_index: int
    def __init__(self, value: _Optional[int] = ..., param_index: _Optional[int] = ..., challenge_index: _Optional[int] = ...) -> None: ...
