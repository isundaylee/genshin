from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ItemHint(_message.Message):
    __slots__ = ("count", "is_new", "item_id", "guid")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    count: int
    is_new: bool
    item_id: int
    guid: int
    def __init__(self, count: _Optional[int] = ..., is_new: bool = ..., item_id: _Optional[int] = ..., guid: _Optional[int] = ...) -> None: ...
