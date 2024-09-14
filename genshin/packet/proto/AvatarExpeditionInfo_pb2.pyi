from genshin.packet.proto import AvatarExpeditionState_pb2 as _AvatarExpeditionState_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarExpeditionInfo(_message.Message):
    __slots__ = ("state", "exp_id", "hour_time", "start_time", "shorten_ratio")
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXP_ID_FIELD_NUMBER: _ClassVar[int]
    HOUR_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    SHORTEN_RATIO_FIELD_NUMBER: _ClassVar[int]
    state: _AvatarExpeditionState_pb2.AvatarExpeditionState
    exp_id: int
    hour_time: int
    start_time: int
    shorten_ratio: float
    def __init__(self, state: _Optional[_Union[_AvatarExpeditionState_pb2.AvatarExpeditionState, str]] = ..., exp_id: _Optional[int] = ..., hour_time: _Optional[int] = ..., start_time: _Optional[int] = ..., shorten_ratio: _Optional[float] = ...) -> None: ...
