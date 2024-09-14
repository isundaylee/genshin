from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeResource(_message.Message):
    __slots__ = ("store_limit", "store_value", "next_refresh_time")
    STORE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    STORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXT_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    store_limit: int
    store_value: int
    next_refresh_time: int
    def __init__(self, store_limit: _Optional[int] = ..., store_value: _Optional[int] = ..., next_refresh_time: _Optional[int] = ...) -> None: ...
