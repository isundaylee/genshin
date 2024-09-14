from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityEmbryo(_message.Message):
    __slots__ = ("ability_id", "ability_name_hash", "ability_override_name_hash")
    ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    ABILITY_NAME_HASH_FIELD_NUMBER: _ClassVar[int]
    ABILITY_OVERRIDE_NAME_HASH_FIELD_NUMBER: _ClassVar[int]
    ability_id: int
    ability_name_hash: int
    ability_override_name_hash: int
    def __init__(self, ability_id: _Optional[int] = ..., ability_name_hash: _Optional[int] = ..., ability_override_name_hash: _Optional[int] = ...) -> None: ...
