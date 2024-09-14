from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GadgetStateNotify(_message.Message):
    __slots__ = ("is_enable_interact", "gadget_state", "gadget_entity_id")
    IS_ENABLE_INTERACT_FIELD_NUMBER: _ClassVar[int]
    GADGET_STATE_FIELD_NUMBER: _ClassVar[int]
    GADGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    is_enable_interact: bool
    gadget_state: int
    gadget_entity_id: int
    def __init__(self, is_enable_interact: bool = ..., gadget_state: _Optional[int] = ..., gadget_entity_id: _Optional[int] = ...) -> None: ...
