from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SceneReliquaryInfo(_message.Message):
    __slots__ = ("item_id", "guid", "level", "promote_level")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    guid: int
    level: int
    promote_level: int
    def __init__(self, item_id: _Optional[int] = ..., guid: _Optional[int] = ..., level: _Optional[int] = ..., promote_level: _Optional[int] = ...) -> None: ...
