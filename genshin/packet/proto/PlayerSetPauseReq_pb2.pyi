from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerSetPauseReq(_message.Message):
    __slots__ = ("is_paused",)
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    is_paused: bool
    def __init__(self, is_paused: bool = ...) -> None: ...
