from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetEquipLockStateRsp(_message.Message):
    __slots__ = ("target_equip_guid", "retcode", "is_locked")
    TARGET_EQUIP_GUID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    target_equip_guid: int
    retcode: int
    is_locked: bool
    def __init__(self, target_equip_guid: _Optional[int] = ..., retcode: _Optional[int] = ..., is_locked: bool = ...) -> None: ...
