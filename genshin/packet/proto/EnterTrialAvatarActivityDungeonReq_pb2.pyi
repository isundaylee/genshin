from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EnterTrialAvatarActivityDungeonReq(_message.Message):
    __slots__ = ("enter_point_id", "activity_id", "trial_avatar_index_id")
    ENTER_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    TRIAL_AVATAR_INDEX_ID_FIELD_NUMBER: _ClassVar[int]
    enter_point_id: int
    activity_id: int
    trial_avatar_index_id: int
    def __init__(self, enter_point_id: _Optional[int] = ..., activity_id: _Optional[int] = ..., trial_avatar_index_id: _Optional[int] = ...) -> None: ...
