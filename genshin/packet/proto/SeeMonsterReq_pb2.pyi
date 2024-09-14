from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SeeMonsterReq(_message.Message):
    __slots__ = ("monster_id",)
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    monster_id: int
    def __init__(self, monster_id: _Optional[int] = ...) -> None: ...
