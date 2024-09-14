from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TowerLevelRecord(_message.Message):
    __slots__ = ("level_id", "satisfied_cond_list")
    LEVEL_ID_FIELD_NUMBER: _ClassVar[int]
    SATISFIED_COND_LIST_FIELD_NUMBER: _ClassVar[int]
    level_id: int
    satisfied_cond_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, level_id: _Optional[int] = ..., satisfied_cond_list: _Optional[_Iterable[int]] = ...) -> None: ...
