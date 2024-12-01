from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EILAAJBHNLD(_message.Message):
    __slots__ = ("prop_map", "MEJLFKPFPGK")
    class PropMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PROP_MAP_FIELD_NUMBER: _ClassVar[int]
    MEJLFKPFPGK_FIELD_NUMBER: _ClassVar[int]
    prop_map: _containers.ScalarMap[int, int]
    MEJLFKPFPGK: int
    def __init__(self, prop_map: _Optional[_Mapping[int, int]] = ..., MEJLFKPFPGK: _Optional[int] = ...) -> None: ...
