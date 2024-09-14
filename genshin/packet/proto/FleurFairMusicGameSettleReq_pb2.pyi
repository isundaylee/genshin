from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FleurFairMusicGameSettleReq(_message.Message):
    __slots__ = ("combo", "music_basic_id", "score", "correct_hit")
    COMBO_FIELD_NUMBER: _ClassVar[int]
    MUSIC_BASIC_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    CORRECT_HIT_FIELD_NUMBER: _ClassVar[int]
    combo: int
    music_basic_id: int
    score: int
    correct_hit: int
    def __init__(self, combo: _Optional[int] = ..., music_basic_id: _Optional[int] = ..., score: _Optional[int] = ..., correct_hit: _Optional[int] = ...) -> None: ...
