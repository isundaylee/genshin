from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetCoolDownData(_message.Message):
    __slots__ = ("id", "cool_down_time", "is_success")
    ID_FIELD_NUMBER: _ClassVar[int]
    COOL_DOWN_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    cool_down_time: int
    is_success: bool
    def __init__(self, id: _Optional[int] = ..., cool_down_time: _Optional[int] = ..., is_success: bool = ...) -> None: ...
