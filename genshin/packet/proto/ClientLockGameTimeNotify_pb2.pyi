from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClientLockGameTimeNotify(_message.Message):
    __slots__ = ("is_lock",)
    IS_LOCK_FIELD_NUMBER: _ClassVar[int]
    is_lock: bool
    def __init__(self, is_lock: bool = ...) -> None: ...
