from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarChangeCostumeRsp(_message.Message):
    __slots__ = ("avatar_guid", "costume_id", "retcode")
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    avatar_guid: int
    costume_id: int
    retcode: int
    def __init__(self, avatar_guid: _Optional[int] = ..., costume_id: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
