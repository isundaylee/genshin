from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EvtAvatarStandUpNotify(_message.Message):
    __slots__ = ("chair_id", "perform_id", "entity_id", "direction")
    CHAIR_ID_FIELD_NUMBER: _ClassVar[int]
    PERFORM_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    chair_id: int
    perform_id: int
    entity_id: int
    direction: int
    def __init__(self, chair_id: _Optional[int] = ..., perform_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., direction: _Optional[int] = ...) -> None: ...
