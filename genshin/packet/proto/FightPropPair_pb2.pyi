from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FightPropPair(_message.Message):
    __slots__ = ("prop_type", "prop_value")
    PROP_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROP_VALUE_FIELD_NUMBER: _ClassVar[int]
    prop_type: int
    prop_value: float
    def __init__(self, prop_type: _Optional[int] = ..., prop_value: _Optional[float] = ...) -> None: ...
