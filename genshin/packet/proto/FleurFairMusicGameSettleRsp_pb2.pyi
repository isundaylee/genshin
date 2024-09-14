from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FleurFairMusicGameSettleRsp(_message.Message):
    __slots__ = ("music_basic_id", "is_new_record", "retcode", "is_unlock_next_level")
    MUSIC_BASIC_ID_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_RECORD_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    IS_UNLOCK_NEXT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    music_basic_id: int
    is_new_record: bool
    retcode: int
    is_unlock_next_level: bool
    def __init__(self, music_basic_id: _Optional[int] = ..., is_new_record: bool = ..., retcode: _Optional[int] = ..., is_unlock_next_level: bool = ...) -> None: ...
