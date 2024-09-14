from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterAIConfigHashNotify(_message.Message):
    __slots__ = ("hash_value", "entity_id", "job_id")
    HASH_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    hash_value: int
    entity_id: int
    job_id: int
    def __init__(self, hash_value: _Optional[int] = ..., entity_id: _Optional[int] = ..., job_id: _Optional[int] = ...) -> None: ...
