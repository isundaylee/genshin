from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ServantInfo(_message.Message):
    __slots__ = ("master_entity_id", "born_slot_index")
    MASTER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    BORN_SLOT_INDEX_FIELD_NUMBER: _ClassVar[int]
    master_entity_id: int
    born_slot_index: int
    def __init__(self, master_entity_id: _Optional[int] = ..., born_slot_index: _Optional[int] = ...) -> None: ...
