from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WearEquipRsp(_message.Message):
    __slots__ = ("avatar_guid", "retcode", "equip_guid")
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    EQUIP_GUID_FIELD_NUMBER: _ClassVar[int]
    avatar_guid: int
    retcode: int
    equip_guid: int
    def __init__(self, avatar_guid: _Optional[int] = ..., retcode: _Optional[int] = ..., equip_guid: _Optional[int] = ...) -> None: ...
