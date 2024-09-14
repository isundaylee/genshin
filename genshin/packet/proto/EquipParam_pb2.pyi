from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EquipParam(_message.Message):
    __slots__ = ("item_id", "item_num", "item_level", "promote_level")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_NUM_FIELD_NUMBER: _ClassVar[int]
    ITEM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    item_num: int
    item_level: int
    promote_level: int
    def __init__(self, item_id: _Optional[int] = ..., item_num: _Optional[int] = ..., item_level: _Optional[int] = ..., promote_level: _Optional[int] = ...) -> None: ...
