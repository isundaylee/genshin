from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerCompoundMaterialReq(_message.Message):
    __slots__ = ("compound_id", "count")
    COMPOUND_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    compound_id: int
    count: int
    def __init__(self, compound_id: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
