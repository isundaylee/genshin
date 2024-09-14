from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassRewardPlanOption(_message.Message):
    __slots__ = ("OCACCJODDDO", "default_reward_type", "IOIHAODNIKF")
    OCACCJODDDO_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_REWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    IOIHAODNIKF_FIELD_NUMBER: _ClassVar[int]
    OCACCJODDDO: bool
    default_reward_type: int
    IOIHAODNIKF: int
    def __init__(self, OCACCJODDDO: bool = ..., default_reward_type: _Optional[int] = ..., IOIHAODNIKF: _Optional[int] = ...) -> None: ...
