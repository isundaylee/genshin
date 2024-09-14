from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OfferingInfo(_message.Message):
    __slots__ = ("offering_id",)
    OFFERING_ID_FIELD_NUMBER: _ClassVar[int]
    offering_id: int
    def __init__(self, offering_id: _Optional[int] = ...) -> None: ...
