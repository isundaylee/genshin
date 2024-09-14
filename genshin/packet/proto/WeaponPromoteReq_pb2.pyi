from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WeaponPromoteReq(_message.Message):
    __slots__ = ("target_weapon_guid",)
    TARGET_WEAPON_GUID_FIELD_NUMBER: _ClassVar[int]
    target_weapon_guid: int
    def __init__(self, target_weapon_guid: _Optional[int] = ...) -> None: ...
