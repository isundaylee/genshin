from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetAllMailNotify(_message.Message):
    __slots__ = ("is_collected",)
    IS_COLLECTED_FIELD_NUMBER: _ClassVar[int]
    is_collected: bool
    def __init__(self, is_collected: bool = ...) -> None: ...
