from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BlossomChestInfo(_message.Message):
    __slots__ = ("resin", "qualify_uid_list", "remain_uid_list", "dead_time", "blossom_refresh_type", "refresh_id")
    RESIN_FIELD_NUMBER: _ClassVar[int]
    QUALIFY_UID_LIST_FIELD_NUMBER: _ClassVar[int]
    REMAIN_UID_LIST_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_FIELD_NUMBER: _ClassVar[int]
    BLOSSOM_REFRESH_TYPE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_ID_FIELD_NUMBER: _ClassVar[int]
    resin: int
    qualify_uid_list: _containers.RepeatedScalarFieldContainer[int]
    remain_uid_list: _containers.RepeatedScalarFieldContainer[int]
    dead_time: int
    blossom_refresh_type: int
    refresh_id: int
    def __init__(self, resin: _Optional[int] = ..., qualify_uid_list: _Optional[_Iterable[int]] = ..., remain_uid_list: _Optional[_Iterable[int]] = ..., dead_time: _Optional[int] = ..., blossom_refresh_type: _Optional[int] = ..., refresh_id: _Optional[int] = ...) -> None: ...
