from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MainCoop(_message.Message):
    __slots__ = ("self_confidence", "status", "save_point_id_list", "id", "GEHNFJEPCJL", "GDBKBKACDFO", "seen_ending_map")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID: _ClassVar[MainCoop.Status]
        RUNNING: _ClassVar[MainCoop.Status]
        FINISHED: _ClassVar[MainCoop.Status]
    INVALID: MainCoop.Status
    RUNNING: MainCoop.Status
    FINISHED: MainCoop.Status
    class GEHNFJEPCJLEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class GDBKBKACDFOEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class SeenEndingMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    SELF_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SAVE_POINT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    GEHNFJEPCJL_FIELD_NUMBER: _ClassVar[int]
    GDBKBKACDFO_FIELD_NUMBER: _ClassVar[int]
    SEEN_ENDING_MAP_FIELD_NUMBER: _ClassVar[int]
    self_confidence: int
    status: MainCoop.Status
    save_point_id_list: _containers.RepeatedScalarFieldContainer[int]
    id: int
    GEHNFJEPCJL: _containers.ScalarMap[int, int]
    GDBKBKACDFO: _containers.ScalarMap[int, int]
    seen_ending_map: _containers.ScalarMap[int, int]
    def __init__(self, self_confidence: _Optional[int] = ..., status: _Optional[_Union[MainCoop.Status, str]] = ..., save_point_id_list: _Optional[_Iterable[int]] = ..., id: _Optional[int] = ..., GEHNFJEPCJL: _Optional[_Mapping[int, int]] = ..., GDBKBKACDFO: _Optional[_Mapping[int, int]] = ..., seen_ending_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
