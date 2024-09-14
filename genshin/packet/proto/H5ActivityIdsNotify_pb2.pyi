from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class H5ActivityIdsNotify(_message.Message):
    __slots__ = ("client_red_dot_timestamp", "h5_activity_map")
    class H5ActivityMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    CLIENT_RED_DOT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    H5_ACTIVITY_MAP_FIELD_NUMBER: _ClassVar[int]
    client_red_dot_timestamp: int
    h5_activity_map: _containers.ScalarMap[int, int]
    def __init__(self, client_red_dot_timestamp: _Optional[int] = ..., h5_activity_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
