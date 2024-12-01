from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MEJFBKGDKOB(_message.Message):
    __slots__ = ("fight_prop_map", "MEJLFKPFPGK")
    class FightPropMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    FIGHT_PROP_MAP_FIELD_NUMBER: _ClassVar[int]
    MEJLFKPFPGK_FIELD_NUMBER: _ClassVar[int]
    fight_prop_map: _containers.ScalarMap[int, float]
    MEJLFKPFPGK: int
    def __init__(self, fight_prop_map: _Optional[_Mapping[int, float]] = ..., MEJLFKPFPGK: _Optional[int] = ...) -> None: ...
