from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SelectWorktopOptionRsp(_message.Message):
    __slots__ = ("option_id", "gadget_entity_id", "retcode")
    OPTION_ID_FIELD_NUMBER: _ClassVar[int]
    GADGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    option_id: int
    gadget_entity_id: int
    retcode: int
    def __init__(self, option_id: _Optional[int] = ..., gadget_entity_id: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
