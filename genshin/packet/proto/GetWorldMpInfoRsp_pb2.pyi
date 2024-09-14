from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetWorldMpInfoRsp(_message.Message):
    __slots__ = ("retcode", "is_in_mp_mode", "quit_mp_valid_time")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    IS_IN_MP_MODE_FIELD_NUMBER: _ClassVar[int]
    QUIT_MP_VALID_TIME_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    is_in_mp_mode: bool
    quit_mp_valid_time: int
    def __init__(self, retcode: _Optional[int] = ..., is_in_mp_mode: bool = ..., quit_mp_valid_time: _Optional[int] = ...) -> None: ...
