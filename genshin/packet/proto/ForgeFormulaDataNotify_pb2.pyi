from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ForgeFormulaDataNotify(_message.Message):
    __slots__ = ("is_locked", "forge_id")
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    FORGE_ID_FIELD_NUMBER: _ClassVar[int]
    is_locked: bool
    forge_id: int
    def __init__(self, is_locked: bool = ..., forge_id: _Optional[int] = ...) -> None: ...
