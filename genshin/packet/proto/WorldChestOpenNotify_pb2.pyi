from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WorldChestOpenNotify(_message.Message):
    __slots__ = ("scene_id", "group_id", "config_id")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    group_id: int
    config_id: int
    def __init__(self, scene_id: _Optional[int] = ..., group_id: _Optional[int] = ..., config_id: _Optional[int] = ...) -> None: ...
