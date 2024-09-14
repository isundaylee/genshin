from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterForceAlertNotify(_message.Message):
    __slots__ = ("monster_entity_id",)
    MONSTER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    monster_entity_id: int
    def __init__(self, monster_entity_id: _Optional[int] = ...) -> None: ...
