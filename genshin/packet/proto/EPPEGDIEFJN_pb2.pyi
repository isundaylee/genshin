from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EPPEGDIEFJN(_message.Message):
    __slots__ = ("costume_id", "JEGIIJCNAFN", "BBPGIJFJHEN", "avatar_id", "level")
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    JEGIIJCNAFN_FIELD_NUMBER: _ClassVar[int]
    BBPGIJFJHEN_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    costume_id: int
    JEGIIJCNAFN: int
    BBPGIJFJHEN: int
    avatar_id: int
    level: int
    def __init__(self, costume_id: _Optional[int] = ..., JEGIIJCNAFN: _Optional[int] = ..., BBPGIJFJHEN: _Optional[int] = ..., avatar_id: _Optional[int] = ..., level: _Optional[int] = ...) -> None: ...
