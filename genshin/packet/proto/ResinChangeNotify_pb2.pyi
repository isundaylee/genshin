from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResinChangeNotify(_message.Message):
    __slots__ = ("cur_value", "cur_buy_count", "next_add_timestamp")
    CUR_VALUE_FIELD_NUMBER: _ClassVar[int]
    CUR_BUY_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_ADD_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    cur_value: int
    cur_buy_count: int
    next_add_timestamp: int
    def __init__(self, cur_value: _Optional[int] = ..., cur_buy_count: _Optional[int] = ..., next_add_timestamp: _Optional[int] = ...) -> None: ...
