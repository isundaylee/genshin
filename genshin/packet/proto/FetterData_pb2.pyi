from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FetterData(_message.Message):
    __slots__ = ("fetter_id", "fetter_state", "cond_index_list")
    FETTER_ID_FIELD_NUMBER: _ClassVar[int]
    FETTER_STATE_FIELD_NUMBER: _ClassVar[int]
    COND_INDEX_LIST_FIELD_NUMBER: _ClassVar[int]
    fetter_id: int
    fetter_state: int
    cond_index_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, fetter_id: _Optional[int] = ..., fetter_state: _Optional[int] = ..., cond_index_list: _Optional[_Iterable[int]] = ...) -> None: ...
