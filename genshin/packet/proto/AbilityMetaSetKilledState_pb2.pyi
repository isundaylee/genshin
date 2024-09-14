from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityMetaSetKilledState(_message.Message):
    __slots__ = ("killed",)
    KILLED_FIELD_NUMBER: _ClassVar[int]
    killed: bool
    def __init__(self, killed: bool = ...) -> None: ...
