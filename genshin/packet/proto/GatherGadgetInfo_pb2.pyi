from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GatherGadgetInfo(_message.Message):
    __slots__ = ("item_id", "is_forbid_guest")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FORBID_GUEST_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    is_forbid_guest: bool
    def __init__(self, item_id: _Optional[int] = ..., is_forbid_guest: bool = ...) -> None: ...
