from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FurnitureMakeData(_message.Message):
    __slots__ = ("make_id", "dur_time", "index", "accelerate_time", "avatar_id", "begin_time")
    MAKE_ID_FIELD_NUMBER: _ClassVar[int]
    DUR_TIME_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ACCELERATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    make_id: int
    dur_time: int
    index: int
    accelerate_time: int
    avatar_id: int
    begin_time: int
    def __init__(self, make_id: _Optional[int] = ..., dur_time: _Optional[int] = ..., index: _Optional[int] = ..., accelerate_time: _Optional[int] = ..., avatar_id: _Optional[int] = ..., begin_time: _Optional[int] = ...) -> None: ...
