from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EnterTrialAvatarActivityDungeonRsp(_message.Message):
    __slots__ = ("activity_id", "retcode", "trial_avatar_index_id")
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    TRIAL_AVATAR_INDEX_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: int
    retcode: int
    trial_avatar_index_id: int
    def __init__(self, activity_id: _Optional[int] = ..., retcode: _Optional[int] = ..., trial_avatar_index_id: _Optional[int] = ...) -> None: ...
