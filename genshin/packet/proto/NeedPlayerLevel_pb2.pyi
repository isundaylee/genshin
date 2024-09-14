from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NeedPlayerLevel(_message.Message):
    __slots__ = ("is_limit", "config_need_player_level")
    IS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_NEED_PLAYER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    is_limit: bool
    config_need_player_level: int
    def __init__(self, is_limit: bool = ..., config_need_player_level: _Optional[int] = ...) -> None: ...
