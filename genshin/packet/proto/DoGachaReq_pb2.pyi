from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DoGachaReq(_message.Message):
    __slots__ = ("gacha_tag", "gacha_schedule_id", "gacha_type", "gacha_random", "gacha_times")
    GACHA_TAG_FIELD_NUMBER: _ClassVar[int]
    GACHA_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    GACHA_TYPE_FIELD_NUMBER: _ClassVar[int]
    GACHA_RANDOM_FIELD_NUMBER: _ClassVar[int]
    GACHA_TIMES_FIELD_NUMBER: _ClassVar[int]
    gacha_tag: str
    gacha_schedule_id: int
    gacha_type: int
    gacha_random: int
    gacha_times: int
    def __init__(self, gacha_tag: _Optional[str] = ..., gacha_schedule_id: _Optional[int] = ..., gacha_type: _Optional[int] = ..., gacha_random: _Optional[int] = ..., gacha_times: _Optional[int] = ...) -> None: ...
