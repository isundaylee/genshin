from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ParentQuestRandomInfo(_message.Message):
    __slots__ = ("factor_list", "template_id", "entrance_id")
    FACTOR_LIST_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRANCE_ID_FIELD_NUMBER: _ClassVar[int]
    factor_list: _containers.RepeatedScalarFieldContainer[int]
    template_id: int
    entrance_id: int
    def __init__(self, factor_list: _Optional[_Iterable[int]] = ..., template_id: _Optional[int] = ..., entrance_id: _Optional[int] = ...) -> None: ...
