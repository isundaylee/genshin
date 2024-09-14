from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MuqadasPotionDungeonSettleNotify(_message.Message):
    __slots__ = ("is_success", "level_id", "is_new_record", "capture_weakness_count", "final_score")
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_RECORD_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_WEAKNESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FINAL_SCORE_FIELD_NUMBER: _ClassVar[int]
    is_success: bool
    level_id: int
    is_new_record: bool
    capture_weakness_count: int
    final_score: int
    def __init__(self, is_success: bool = ..., level_id: _Optional[int] = ..., is_new_record: bool = ..., capture_weakness_count: _Optional[int] = ..., final_score: _Optional[int] = ...) -> None: ...
