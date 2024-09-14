from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarDelNotify(_message.Message):
    __slots__ = ("avatar_guid_list",)
    AVATAR_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    avatar_guid_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, avatar_guid_list: _Optional[_Iterable[int]] = ...) -> None: ...
