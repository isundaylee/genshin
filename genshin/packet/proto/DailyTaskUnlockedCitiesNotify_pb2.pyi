from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DailyTaskUnlockedCitiesNotify(_message.Message):
    __slots__ = ("unlocked_city_list",)
    UNLOCKED_CITY_LIST_FIELD_NUMBER: _ClassVar[int]
    unlocked_city_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, unlocked_city_list: _Optional[_Iterable[int]] = ...) -> None: ...
