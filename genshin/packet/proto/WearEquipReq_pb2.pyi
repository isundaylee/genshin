from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WearEquipReq(_message.Message):
    __slots__ = ("equip_guid", "avatar_guid")
    EQUIP_GUID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    equip_guid: int
    avatar_guid: int
    def __init__(self, equip_guid: _Optional[int] = ..., avatar_guid: _Optional[int] = ...) -> None: ...
