from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerPropChangeNotify(_message.Message):
    __slots__ = ("prop_delta", "prop_type")
    PROP_DELTA_FIELD_NUMBER: _ClassVar[int]
    PROP_TYPE_FIELD_NUMBER: _ClassVar[int]
    prop_delta: int
    prop_type: int
    def __init__(self, prop_delta: _Optional[int] = ..., prop_type: _Optional[int] = ...) -> None: ...
