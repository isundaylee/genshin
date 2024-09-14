from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonChallengeBeginNotify(_message.Message):
    __slots__ = ("param_list", "challenge_index", "father_index", "uid_list", "challenge_id", "group_id")
    PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_INDEX_FIELD_NUMBER: _ClassVar[int]
    FATHER_INDEX_FIELD_NUMBER: _ClassVar[int]
    UID_LIST_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    param_list: _containers.RepeatedScalarFieldContainer[int]
    challenge_index: int
    father_index: int
    uid_list: _containers.RepeatedScalarFieldContainer[int]
    challenge_id: int
    group_id: int
    def __init__(self, param_list: _Optional[_Iterable[int]] = ..., challenge_index: _Optional[int] = ..., father_index: _Optional[int] = ..., uid_list: _Optional[_Iterable[int]] = ..., challenge_id: _Optional[int] = ..., group_id: _Optional[int] = ...) -> None: ...
