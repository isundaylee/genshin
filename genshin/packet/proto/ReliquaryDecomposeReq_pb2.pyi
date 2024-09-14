from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReliquaryDecomposeReq(_message.Message):
    __slots__ = ("target_count", "guid_list", "config_id")
    TARGET_COUNT_FIELD_NUMBER: _ClassVar[int]
    GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    target_count: int
    guid_list: _containers.RepeatedScalarFieldContainer[int]
    config_id: int
    def __init__(self, target_count: _Optional[int] = ..., guid_list: _Optional[_Iterable[int]] = ..., config_id: _Optional[int] = ...) -> None: ...
