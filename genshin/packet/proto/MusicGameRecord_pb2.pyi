from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MusicGameRecord(_message.Message):
    __slots__ = ("max_combo", "is_unlock", "max_score")
    MAX_COMBO_FIELD_NUMBER: _ClassVar[int]
    IS_UNLOCK_FIELD_NUMBER: _ClassVar[int]
    MAX_SCORE_FIELD_NUMBER: _ClassVar[int]
    max_combo: int
    is_unlock: bool
    max_score: int
    def __init__(self, max_combo: _Optional[int] = ..., is_unlock: bool = ..., max_score: _Optional[int] = ...) -> None: ...
