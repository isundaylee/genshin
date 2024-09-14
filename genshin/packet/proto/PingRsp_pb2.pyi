from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PingRsp(_message.Message):
    __slots__ = ("seq", "client_time", "retcode")
    SEQ_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TIME_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    seq: int
    client_time: int
    retcode: int
    def __init__(self, seq: _Optional[int] = ..., client_time: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
