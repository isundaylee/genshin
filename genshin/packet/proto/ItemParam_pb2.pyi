from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ItemParam(_message.Message):
    __slots__ = ("item_id", "count")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    count: int
    def __init__(self, item_id: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
