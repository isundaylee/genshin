from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MaterialInfo(_message.Message):
    __slots__ = ("count", "guid")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    count: int
    guid: int
    def __init__(self, count: _Optional[int] = ..., guid: _Optional[int] = ...) -> None: ...
