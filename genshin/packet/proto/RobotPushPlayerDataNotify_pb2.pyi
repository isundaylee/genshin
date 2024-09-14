from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RobotPushPlayerDataNotify(_message.Message):
    __slots__ = ("bin",)
    BIN_FIELD_NUMBER: _ClassVar[int]
    bin: bytes
    def __init__(self, bin: _Optional[bytes] = ...) -> None: ...
