from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MusicGameStartReq(_message.Message):
    __slots__ = ("ugc_guid", "music_basic_id", "is_save_score")
    UGC_GUID_FIELD_NUMBER: _ClassVar[int]
    MUSIC_BASIC_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SAVE_SCORE_FIELD_NUMBER: _ClassVar[int]
    ugc_guid: int
    music_basic_id: int
    is_save_score: bool
    def __init__(self, ugc_guid: _Optional[int] = ..., music_basic_id: _Optional[int] = ..., is_save_score: bool = ...) -> None: ...
