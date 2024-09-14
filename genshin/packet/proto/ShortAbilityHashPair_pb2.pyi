from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ShortAbilityHashPair(_message.Message):
    __slots__ = ("OMPEBEMNKLG", "ability_name_hash")
    OMPEBEMNKLG_FIELD_NUMBER: _ClassVar[int]
    ABILITY_NAME_HASH_FIELD_NUMBER: _ClassVar[int]
    OMPEBEMNKLG: int
    ability_name_hash: int
    def __init__(self, OMPEBEMNKLG: _Optional[int] = ..., ability_name_hash: _Optional[int] = ...) -> None: ...
