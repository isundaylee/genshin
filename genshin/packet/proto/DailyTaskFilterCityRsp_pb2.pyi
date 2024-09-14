from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DailyTaskFilterCityRsp(_message.Message):
    __slots__ = ("city_id", "retcode")
    CITY_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    city_id: int
    retcode: int
    def __init__(self, city_id: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
