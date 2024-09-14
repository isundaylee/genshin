from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScreenInfo(_message.Message):
    __slots__ = ("live_id", "projector_entity_id")
    LIVE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECTOR_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    live_id: int
    projector_entity_id: int
    def __init__(self, live_id: _Optional[int] = ..., projector_entity_id: _Optional[int] = ...) -> None: ...
