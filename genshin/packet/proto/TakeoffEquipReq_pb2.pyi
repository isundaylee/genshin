from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TakeoffEquipReq(_message.Message):
    __slots__ = ("avatar_guid", "slot")
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    avatar_guid: int
    slot: int
    def __init__(self, avatar_guid: _Optional[int] = ..., slot: _Optional[int] = ...) -> None: ...
