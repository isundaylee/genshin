from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AiSyncInfo(_message.Message):
    __slots__ = ("has_path_to_target", "is_self_killing", "entity_id")
    HAS_PATH_TO_TARGET_FIELD_NUMBER: _ClassVar[int]
    IS_SELF_KILLING_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    has_path_to_target: bool
    is_self_killing: bool
    entity_id: int
    def __init__(self, has_path_to_target: bool = ..., is_self_killing: bool = ..., entity_id: _Optional[int] = ...) -> None: ...
