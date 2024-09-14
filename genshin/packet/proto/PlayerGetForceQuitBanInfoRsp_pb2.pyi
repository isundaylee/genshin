from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerGetForceQuitBanInfoRsp(_message.Message):
    __slots__ = ("match_id", "retcode", "expire_time")
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    match_id: int
    retcode: int
    expire_time: int
    def __init__(self, match_id: _Optional[int] = ..., retcode: _Optional[int] = ..., expire_time: _Optional[int] = ...) -> None: ...
