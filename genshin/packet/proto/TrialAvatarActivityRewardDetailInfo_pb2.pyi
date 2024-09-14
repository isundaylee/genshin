from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TrialAvatarActivityRewardDetailInfo(_message.Message):
    __slots__ = ("passed_dungeon", "reward_id", "received_reward", "trial_avatar_index_id")
    PASSED_DUNGEON_FIELD_NUMBER: _ClassVar[int]
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_REWARD_FIELD_NUMBER: _ClassVar[int]
    TRIAL_AVATAR_INDEX_ID_FIELD_NUMBER: _ClassVar[int]
    passed_dungeon: bool
    reward_id: int
    received_reward: bool
    trial_avatar_index_id: int
    def __init__(self, passed_dungeon: bool = ..., reward_id: _Optional[int] = ..., received_reward: bool = ..., trial_avatar_index_id: _Optional[int] = ...) -> None: ...
