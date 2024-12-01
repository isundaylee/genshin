from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NPLAPCBPPMF(_message.Message):
    __slots__ = ("BBPGIJFJHEN", "avatar_id")
    BBPGIJFJHEN_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    BBPGIJFJHEN: int
    avatar_id: int
    def __init__(self, BBPGIJFJHEN: _Optional[int] = ..., avatar_id: _Optional[int] = ...) -> None: ...
