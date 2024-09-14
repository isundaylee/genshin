from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GachaWishReq(_message.Message):
    __slots__ = ("gacha_type", "gacha_schedule_id", "item_id")
    GACHA_TYPE_FIELD_NUMBER: _ClassVar[int]
    GACHA_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    gacha_type: int
    gacha_schedule_id: int
    item_id: int
    def __init__(self, gacha_type: _Optional[int] = ..., gacha_schedule_id: _Optional[int] = ..., item_id: _Optional[int] = ...) -> None: ...
