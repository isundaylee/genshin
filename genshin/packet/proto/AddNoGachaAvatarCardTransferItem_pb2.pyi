from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddNoGachaAvatarCardTransferItem(_message.Message):
    __slots__ = ("count", "item_id", "is_new")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_FIELD_NUMBER: _ClassVar[int]
    count: int
    item_id: int
    is_new: bool
    def __init__(self, count: _Optional[int] = ..., item_id: _Optional[int] = ..., is_new: bool = ...) -> None: ...
