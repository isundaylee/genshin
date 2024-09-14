from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ServerTimeNotify(_message.Message):
    __slots__ = ("server_time",)
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    server_time: int
    def __init__(self, server_time: _Optional[int] = ...) -> None: ...
