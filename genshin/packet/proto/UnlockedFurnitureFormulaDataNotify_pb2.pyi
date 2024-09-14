from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnlockedFurnitureFormulaDataNotify(_message.Message):
    __slots__ = ("is_all", "furniture_id_list")
    IS_ALL_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    is_all: bool
    furniture_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, is_all: bool = ..., furniture_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
