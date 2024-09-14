from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VehicleMember(_message.Message):
    __slots__ = ("uid", "avatar_guid", "pos")
    UID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    uid: int
    avatar_guid: int
    pos: int
    def __init__(self, uid: _Optional[int] = ..., avatar_guid: _Optional[int] = ..., pos: _Optional[int] = ...) -> None: ...
