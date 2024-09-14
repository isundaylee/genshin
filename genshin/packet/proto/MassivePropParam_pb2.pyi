from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MassivePropParam(_message.Message):
    __slots__ = ("type", "reaction_info_list", "param_list", "sync_flag")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REACTION_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    SYNC_FLAG_FIELD_NUMBER: _ClassVar[int]
    type: int
    reaction_info_list: _containers.RepeatedScalarFieldContainer[int]
    param_list: _containers.RepeatedScalarFieldContainer[float]
    sync_flag: int
    def __init__(self, type: _Optional[int] = ..., reaction_info_list: _Optional[_Iterable[int]] = ..., param_list: _Optional[_Iterable[float]] = ..., sync_flag: _Optional[int] = ...) -> None: ...
