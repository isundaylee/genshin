from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonWayPointNotify(_message.Message):
    __slots__ = ("is_add", "active_way_point_list")
    IS_ADD_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_WAY_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    is_add: bool
    active_way_point_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, is_add: bool = ..., active_way_point_list: _Optional[_Iterable[int]] = ...) -> None: ...
