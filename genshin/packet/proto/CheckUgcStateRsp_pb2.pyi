from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CheckUgcStateRsp(_message.Message):
    __slots__ = ("retcode",)
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    def __init__(self, retcode: _Optional[int] = ...) -> None: ...
