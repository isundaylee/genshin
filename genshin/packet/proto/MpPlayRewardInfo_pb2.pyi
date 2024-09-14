from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MpPlayRewardInfo(_message.Message):
    __slots__ = ("resin", "remain_uid_list", "qualify_uid_list")
    RESIN_FIELD_NUMBER: _ClassVar[int]
    REMAIN_UID_LIST_FIELD_NUMBER: _ClassVar[int]
    QUALIFY_UID_LIST_FIELD_NUMBER: _ClassVar[int]
    resin: int
    remain_uid_list: _containers.RepeatedScalarFieldContainer[int]
    qualify_uid_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, resin: _Optional[int] = ..., remain_uid_list: _Optional[_Iterable[int]] = ..., qualify_uid_list: _Optional[_Iterable[int]] = ...) -> None: ...
