from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KBOMELDKJGK(_message.Message):
    __slots__ = ("avatar_id",)
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, avatar_id: _Optional[_Iterable[int]] = ...) -> None: ...
