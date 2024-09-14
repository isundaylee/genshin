from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityGadgetInfo(_message.Message):
    __slots__ = ("camp_id", "camp_target_type", "target_entity_id")
    CAMP_ID_FIELD_NUMBER: _ClassVar[int]
    CAMP_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    camp_id: int
    camp_target_type: int
    target_entity_id: int
    def __init__(self, camp_id: _Optional[int] = ..., camp_target_type: _Optional[int] = ..., target_entity_id: _Optional[int] = ...) -> None: ...
