from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarExpeditionStartReq(_message.Message):
    __slots__ = ("avatar_guid", "hour_time", "exp_id")
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    HOUR_TIME_FIELD_NUMBER: _ClassVar[int]
    EXP_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_guid: int
    hour_time: int
    exp_id: int
    def __init__(self, avatar_guid: _Optional[int] = ..., hour_time: _Optional[int] = ..., exp_id: _Optional[int] = ...) -> None: ...
