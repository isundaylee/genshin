from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FishPoolInfo(_message.Message):
    __slots__ = ("pool_id", "fish_area_list", "today_fish_num")
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    FISH_AREA_LIST_FIELD_NUMBER: _ClassVar[int]
    TODAY_FISH_NUM_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    fish_area_list: _containers.RepeatedScalarFieldContainer[int]
    today_fish_num: int
    def __init__(self, pool_id: _Optional[int] = ..., fish_area_list: _Optional[_Iterable[int]] = ..., today_fish_num: _Optional[int] = ...) -> None: ...
