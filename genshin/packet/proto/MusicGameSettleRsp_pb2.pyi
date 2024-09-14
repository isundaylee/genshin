from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MusicGameSettleRsp(_message.Message):
    __slots__ = ("ugc_guid", "retcode", "music_basic_id", "is_unlock_next_level", "is_new_record")
    UGC_GUID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    MUSIC_BASIC_ID_FIELD_NUMBER: _ClassVar[int]
    IS_UNLOCK_NEXT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_RECORD_FIELD_NUMBER: _ClassVar[int]
    ugc_guid: int
    retcode: int
    music_basic_id: int
    is_unlock_next_level: bool
    is_new_record: bool
    def __init__(self, ugc_guid: _Optional[int] = ..., retcode: _Optional[int] = ..., music_basic_id: _Optional[int] = ..., is_unlock_next_level: bool = ..., is_new_record: bool = ...) -> None: ...
