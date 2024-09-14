from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UseItemReq(_message.Message):
    __slots__ = ("count", "option_idx", "target_guid", "is_enter_mp_dungeon_team", "guid")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    OPTION_IDX_FIELD_NUMBER: _ClassVar[int]
    TARGET_GUID_FIELD_NUMBER: _ClassVar[int]
    IS_ENTER_MP_DUNGEON_TEAM_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    count: int
    option_idx: int
    target_guid: int
    is_enter_mp_dungeon_team: bool
    guid: int
    def __init__(self, count: _Optional[int] = ..., option_idx: _Optional[int] = ..., target_guid: _Optional[int] = ..., is_enter_mp_dungeon_team: bool = ..., guid: _Optional[int] = ...) -> None: ...
