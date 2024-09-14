from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarSatiationData(_message.Message):
    __slots__ = ("penalty_finish_time", "avatar_guid", "finish_time")
    PENALTY_FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    penalty_finish_time: float
    avatar_guid: int
    finish_time: float
    def __init__(self, penalty_finish_time: _Optional[float] = ..., avatar_guid: _Optional[int] = ..., finish_time: _Optional[float] = ...) -> None: ...
