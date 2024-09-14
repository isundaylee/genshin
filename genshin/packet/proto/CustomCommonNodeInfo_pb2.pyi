from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CustomCommonNodeInfo(_message.Message):
    __slots__ = ("parent_index", "config_id", "slot_identifier", "param_list")
    PARENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    parent_index: int
    config_id: int
    slot_identifier: str
    param_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, parent_index: _Optional[int] = ..., config_id: _Optional[int] = ..., slot_identifier: _Optional[str] = ..., param_list: _Optional[_Iterable[int]] = ...) -> None: ...
