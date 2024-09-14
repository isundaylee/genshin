from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MarkNewNotify(_message.Message):
    __slots__ = ("id_list", "mark_new_type")
    ID_LIST_FIELD_NUMBER: _ClassVar[int]
    MARK_NEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    id_list: _containers.RepeatedScalarFieldContainer[int]
    mark_new_type: int
    def __init__(self, id_list: _Optional[_Iterable[int]] = ..., mark_new_type: _Optional[int] = ...) -> None: ...
