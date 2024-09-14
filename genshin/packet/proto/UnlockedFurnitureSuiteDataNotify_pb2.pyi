from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnlockedFurnitureSuiteDataNotify(_message.Message):
    __slots__ = ("furniture_suite_id_list", "is_all")
    FURNITURE_SUITE_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_ALL_FIELD_NUMBER: _ClassVar[int]
    furniture_suite_id_list: _containers.RepeatedScalarFieldContainer[int]
    is_all: bool
    def __init__(self, furniture_suite_id_list: _Optional[_Iterable[int]] = ..., is_all: bool = ...) -> None: ...
