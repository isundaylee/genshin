from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EEOIOGPEODJ(_message.Message):
    __slots__ = ("bgm_id", "red_point", "is_show_brief_card_event_case", "is_show_animation", "is_show_detail_build")
    BGM_ID_FIELD_NUMBER: _ClassVar[int]
    RED_POINT_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_BRIEF_CARD_EVENT_CASE_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_ANIMATION_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_DETAIL_BUILD_FIELD_NUMBER: _ClassVar[int]
    bgm_id: int
    red_point: int
    is_show_brief_card_event_case: bool
    is_show_animation: bool
    is_show_detail_build: bool
    def __init__(self, bgm_id: _Optional[int] = ..., red_point: _Optional[int] = ..., is_show_brief_card_event_case: bool = ..., is_show_animation: bool = ..., is_show_detail_build: bool = ...) -> None: ...
