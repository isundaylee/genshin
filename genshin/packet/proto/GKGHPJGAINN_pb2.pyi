from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GKGHPJGAINN(_message.Message):
    __slots__ = ("equip_guid_list", "is_locked")
    EQUIP_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    equip_guid_list: _containers.RepeatedScalarFieldContainer[int]
    is_locked: bool
    def __init__(self, equip_guid_list: _Optional[_Iterable[int]] = ..., is_locked: bool = ...) -> None: ...
