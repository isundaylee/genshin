from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SocialShowAvatarInfo(_message.Message):
    __slots__ = ("avatar_id", "level", "costume_id", "AEPNHMCDBFL", "CMAFEKGPACG")
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    AEPNHMCDBFL_FIELD_NUMBER: _ClassVar[int]
    CMAFEKGPACG_FIELD_NUMBER: _ClassVar[int]
    avatar_id: int
    level: int
    costume_id: int
    AEPNHMCDBFL: int
    CMAFEKGPACG: int
    def __init__(self, avatar_id: _Optional[int] = ..., level: _Optional[int] = ..., costume_id: _Optional[int] = ..., AEPNHMCDBFL: _Optional[int] = ..., CMAFEKGPACG: _Optional[int] = ...) -> None: ...
