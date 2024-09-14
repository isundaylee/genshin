from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StatueGadgetInfo(_message.Message):
    __slots__ = ("opened_statue_uid_list",)
    OPENED_STATUE_UID_LIST_FIELD_NUMBER: _ClassVar[int]
    opened_statue_uid_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, opened_statue_uid_list: _Optional[_Iterable[int]] = ...) -> None: ...
