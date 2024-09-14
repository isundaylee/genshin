from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MapAreaInfo(_message.Message):
    __slots__ = ("map_area_id", "is_open")
    MAP_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    map_area_id: int
    is_open: bool
    def __init__(self, map_area_id: _Optional[int] = ..., is_open: bool = ...) -> None: ...
