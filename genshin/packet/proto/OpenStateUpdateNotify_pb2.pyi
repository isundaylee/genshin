from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OpenStateUpdateNotify(_message.Message):
    __slots__ = ("open_state_map",)
    class OpenStateMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    OPEN_STATE_MAP_FIELD_NUMBER: _ClassVar[int]
    open_state_map: _containers.ScalarMap[int, int]
    def __init__(self, open_state_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
