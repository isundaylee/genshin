from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClientAIStateNotify(_message.Message):
    __slots__ = ("cur_tactic", "entity_id")
    CUR_TACTIC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    cur_tactic: int
    entity_id: int
    def __init__(self, cur_tactic: _Optional[int] = ..., entity_id: _Optional[int] = ...) -> None: ...
