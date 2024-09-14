from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NeedBeginTime(_message.Message):
    __slots__ = ("config_need_begin_time", "is_limit")
    CONFIG_NEED_BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    config_need_begin_time: int
    is_limit: bool
    def __init__(self, config_need_begin_time: _Optional[int] = ..., is_limit: bool = ...) -> None: ...
