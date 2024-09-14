from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GachaWishRsp(_message.Message):
    __slots__ = ("gacha_schedule_id", "gacha_type", "retcode", "wishItemId", "wishMaxProgress", "wishProgress")
    GACHA_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    GACHA_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    WISHITEMID_FIELD_NUMBER: _ClassVar[int]
    WISHMAXPROGRESS_FIELD_NUMBER: _ClassVar[int]
    WISHPROGRESS_FIELD_NUMBER: _ClassVar[int]
    gacha_schedule_id: int
    gacha_type: int
    retcode: int
    wishItemId: int
    wishMaxProgress: int
    wishProgress: int
    def __init__(self, gacha_schedule_id: _Optional[int] = ..., gacha_type: _Optional[int] = ..., retcode: _Optional[int] = ..., wishItemId: _Optional[int] = ..., wishMaxProgress: _Optional[int] = ..., wishProgress: _Optional[int] = ...) -> None: ...
