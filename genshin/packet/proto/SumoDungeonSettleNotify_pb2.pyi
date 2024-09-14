from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SumoDungeonSettleNotify(_message.Message):
    __slots__ = ("difficulty_id", "DEJJPIOCJDD", "final_score", "KDPNBLFJKND", "is_new_record", "stage_id")
    DIFFICULTY_ID_FIELD_NUMBER: _ClassVar[int]
    DEJJPIOCJDD_FIELD_NUMBER: _ClassVar[int]
    FINAL_SCORE_FIELD_NUMBER: _ClassVar[int]
    KDPNBLFJKND_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_RECORD_FIELD_NUMBER: _ClassVar[int]
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    difficulty_id: int
    DEJJPIOCJDD: int
    final_score: int
    KDPNBLFJKND: int
    is_new_record: bool
    stage_id: int
    def __init__(self, difficulty_id: _Optional[int] = ..., DEJJPIOCJDD: _Optional[int] = ..., final_score: _Optional[int] = ..., KDPNBLFJKND: _Optional[int] = ..., is_new_record: bool = ..., stage_id: _Optional[int] = ...) -> None: ...
