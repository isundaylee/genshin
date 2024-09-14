from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FurnitureMakeMakeInfo(_message.Message):
    __slots__ = ("furniture_id", "make_count")
    FURNITURE_ID_FIELD_NUMBER: _ClassVar[int]
    MAKE_COUNT_FIELD_NUMBER: _ClassVar[int]
    furniture_id: int
    make_count: int
    def __init__(self, furniture_id: _Optional[int] = ..., make_count: _Optional[int] = ...) -> None: ...
