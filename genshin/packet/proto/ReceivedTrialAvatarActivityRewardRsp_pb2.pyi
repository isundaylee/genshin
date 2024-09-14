from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReceivedTrialAvatarActivityRewardRsp(_message.Message):
    __slots__ = ("retcode", "trial_avatar_index_id", "activity_id")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    TRIAL_AVATAR_INDEX_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    trial_avatar_index_id: int
    activity_id: int
    def __init__(self, retcode: _Optional[int] = ..., trial_avatar_index_id: _Optional[int] = ..., activity_id: _Optional[int] = ...) -> None: ...
