from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SelectWorktopOptionReq(_message.Message):
    __slots__ = ("CHDDOFMLBLM", "gadget_entity_id", "option_id")
    CHDDOFMLBLM_FIELD_NUMBER: _ClassVar[int]
    GADGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    OPTION_ID_FIELD_NUMBER: _ClassVar[int]
    CHDDOFMLBLM: int
    gadget_entity_id: int
    option_id: int
    def __init__(self, CHDDOFMLBLM: _Optional[int] = ..., gadget_entity_id: _Optional[int] = ..., option_id: _Optional[int] = ...) -> None: ...
