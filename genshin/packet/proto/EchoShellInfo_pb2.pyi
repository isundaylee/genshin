from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EchoShellInfo(_message.Message):
    __slots__ = ("shell_id",)
    SHELL_ID_FIELD_NUMBER: _ClassVar[int]
    shell_id: int
    def __init__(self, shell_id: _Optional[int] = ...) -> None: ...
