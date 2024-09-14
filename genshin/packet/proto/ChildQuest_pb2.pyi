from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChildQuest(_message.Message):
    __slots__ = ("quest_config_id", "quest_id", "state")
    QUEST_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    quest_config_id: int
    quest_id: int
    state: int
    def __init__(self, quest_config_id: _Optional[int] = ..., quest_id: _Optional[int] = ..., state: _Optional[int] = ...) -> None: ...
