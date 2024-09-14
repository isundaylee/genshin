from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AnnounceData(_message.Message):
    __slots__ = ("end_time", "count_down_frequency", "dungeon_confirm_text", "count_down_text", "center_system_frequency", "is_center_system_last5_every_minutes", "center_system_text", "begin_time", "config_id")
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    COUNT_DOWN_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_CONFIRM_TEXT_FIELD_NUMBER: _ClassVar[int]
    COUNT_DOWN_TEXT_FIELD_NUMBER: _ClassVar[int]
    CENTER_SYSTEM_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    IS_CENTER_SYSTEM_LAST5_EVERY_MINUTES_FIELD_NUMBER: _ClassVar[int]
    CENTER_SYSTEM_TEXT_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    end_time: int
    count_down_frequency: int
    dungeon_confirm_text: str
    count_down_text: str
    center_system_frequency: int
    is_center_system_last5_every_minutes: bool
    center_system_text: str
    begin_time: int
    config_id: int
    def __init__(self, end_time: _Optional[int] = ..., count_down_frequency: _Optional[int] = ..., dungeon_confirm_text: _Optional[str] = ..., count_down_text: _Optional[str] = ..., center_system_frequency: _Optional[int] = ..., is_center_system_last5_every_minutes: bool = ..., center_system_text: _Optional[str] = ..., begin_time: _Optional[int] = ..., config_id: _Optional[int] = ...) -> None: ...
