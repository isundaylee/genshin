from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarPromoteRsp(_message.Message):
    __slots__ = ("guid", "retcode")
    GUID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    guid: int
    retcode: int
    def __init__(self, guid: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
