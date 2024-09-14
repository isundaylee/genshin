from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetEquipLockStateReq(_message.Message):
    __slots__ = ("is_locked", "target_equip_guid")
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    TARGET_EQUIP_GUID_FIELD_NUMBER: _ClassVar[int]
    is_locked: bool
    target_equip_guid: int
    def __init__(self, is_locked: bool = ..., target_equip_guid: _Optional[int] = ...) -> None: ...
