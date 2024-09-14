from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TowerLevelStarCondData(_message.Message):
    __slots__ = ("is_fail", "is_pause", "cond_value", "star_cond_index")
    IS_FAIL_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSE_FIELD_NUMBER: _ClassVar[int]
    COND_VALUE_FIELD_NUMBER: _ClassVar[int]
    STAR_COND_INDEX_FIELD_NUMBER: _ClassVar[int]
    is_fail: bool
    is_pause: bool
    cond_value: int
    star_cond_index: int
    def __init__(self, is_fail: bool = ..., is_pause: bool = ..., cond_value: _Optional[int] = ..., star_cond_index: _Optional[int] = ...) -> None: ...
