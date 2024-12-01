from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EJOBMPBBBIA(_message.Message):
    __slots__ = ("guid", "level", "promote_level", "item_id")
    GUID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    guid: int
    level: int
    promote_level: int
    item_id: int
    def __init__(self, guid: _Optional[int] = ..., level: _Optional[int] = ..., promote_level: _Optional[int] = ..., item_id: _Optional[int] = ...) -> None: ...
