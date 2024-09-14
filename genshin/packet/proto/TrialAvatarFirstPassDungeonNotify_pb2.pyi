from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TrialAvatarFirstPassDungeonNotify(_message.Message):
    __slots__ = ("trial_avatar_index_id",)
    TRIAL_AVATAR_INDEX_ID_FIELD_NUMBER: _ClassVar[int]
    trial_avatar_index_id: int
    def __init__(self, trial_avatar_index_id: _Optional[int] = ...) -> None: ...
