from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarExpeditionCallBackReq(_message.Message):
    __slots__ = ("avatar_guid",)
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    avatar_guid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, avatar_guid: _Optional[_Iterable[int]] = ...) -> None: ...
