from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TakeCompoundOutputReq(_message.Message):
    __slots__ = ("compound_group_id", "compound_id")
    COMPOUND_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    COMPOUND_ID_FIELD_NUMBER: _ClassVar[int]
    compound_group_id: int
    compound_id: int
    def __init__(self, compound_group_id: _Optional[int] = ..., compound_id: _Optional[int] = ...) -> None: ...
