from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CityInfo(_message.Message):
    __slots__ = ("crystal_num", "city_id", "level")
    CRYSTAL_NUM_FIELD_NUMBER: _ClassVar[int]
    CITY_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    crystal_num: int
    city_id: int
    level: int
    def __init__(self, crystal_num: _Optional[int] = ..., city_id: _Optional[int] = ..., level: _Optional[int] = ...) -> None: ...
