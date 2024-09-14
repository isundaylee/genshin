from genshin.packet.proto import BattlePassUnlockStatus_pb2 as _BattlePassUnlockStatus_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassRewardTag(_message.Message):
    __slots__ = ("DJCKCHACLME", "unlock_status", "level", "reward_id")
    DJCKCHACLME_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_STATUS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    DJCKCHACLME: int
    unlock_status: _BattlePassUnlockStatus_pb2.BattlePassUnlockStatus
    level: int
    reward_id: int
    def __init__(self, DJCKCHACLME: _Optional[int] = ..., unlock_status: _Optional[_Union[_BattlePassUnlockStatus_pb2.BattlePassUnlockStatus, str]] = ..., level: _Optional[int] = ..., reward_id: _Optional[int] = ...) -> None: ...
