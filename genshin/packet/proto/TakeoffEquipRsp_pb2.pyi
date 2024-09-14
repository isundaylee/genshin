from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TakeoffEquipRsp(_message.Message):
    __slots__ = ("avatar_guid", "slot", "retcode")
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    avatar_guid: int
    slot: int
    retcode: int
    def __init__(self, avatar_guid: _Optional[int] = ..., slot: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
