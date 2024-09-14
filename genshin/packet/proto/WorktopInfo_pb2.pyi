from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WorktopInfo(_message.Message):
    __slots__ = ("option_list", "is_guest_can_operate")
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_GUEST_CAN_OPERATE_FIELD_NUMBER: _ClassVar[int]
    option_list: _containers.RepeatedScalarFieldContainer[int]
    is_guest_can_operate: bool
    def __init__(self, option_list: _Optional[_Iterable[int]] = ..., is_guest_can_operate: bool = ...) -> None: ...
