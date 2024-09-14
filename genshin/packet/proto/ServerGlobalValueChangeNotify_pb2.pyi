from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ServerGlobalValueChangeNotify(_message.Message):
    __slots__ = ("key_hash", "entity_id", "value")
    KEY_HASH_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key_hash: int
    entity_id: int
    value: float
    def __init__(self, key_hash: _Optional[int] = ..., entity_id: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
