from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityActionSetRandomOverrideMapValue(_message.Message):
    __slots__ = ("random_value",)
    RANDOM_VALUE_FIELD_NUMBER: _ClassVar[int]
    random_value: float
    def __init__(self, random_value: _Optional[float] = ...) -> None: ...
