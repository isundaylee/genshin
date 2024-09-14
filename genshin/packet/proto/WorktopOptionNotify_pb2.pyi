from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WorktopOptionNotify(_message.Message):
    __slots__ = ("gadget_entity_id", "option_list")
    GADGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    gadget_entity_id: int
    option_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, gadget_entity_id: _Optional[int] = ..., option_list: _Optional[_Iterable[int]] = ...) -> None: ...
