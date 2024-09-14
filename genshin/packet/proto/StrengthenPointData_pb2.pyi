from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StrengthenPointData(_message.Message):
    __slots__ = ("base_point", "cur_point")
    BASE_POINT_FIELD_NUMBER: _ClassVar[int]
    CUR_POINT_FIELD_NUMBER: _ClassVar[int]
    base_point: int
    cur_point: int
    def __init__(self, base_point: _Optional[int] = ..., cur_point: _Optional[int] = ...) -> None: ...
