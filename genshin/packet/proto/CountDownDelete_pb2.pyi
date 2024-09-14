from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CountDownDelete(_message.Message):
    __slots__ = ("delete_time_num_map", "config_count_down_time")
    class DeleteTimeNumMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    DELETE_TIME_NUM_MAP_FIELD_NUMBER: _ClassVar[int]
    CONFIG_COUNT_DOWN_TIME_FIELD_NUMBER: _ClassVar[int]
    delete_time_num_map: _containers.ScalarMap[int, int]
    config_count_down_time: int
    def __init__(self, delete_time_num_map: _Optional[_Mapping[int, int]] = ..., config_count_down_time: _Optional[int] = ...) -> None: ...
