from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AiThreatInfo(_message.Message):
    __slots__ = ("ai_threat_map",)
    class AiThreatMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    AI_THREAT_MAP_FIELD_NUMBER: _ClassVar[int]
    ai_threat_map: _containers.ScalarMap[int, int]
    def __init__(self, ai_threat_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
