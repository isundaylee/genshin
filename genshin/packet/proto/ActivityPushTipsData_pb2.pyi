from genshin.packet.proto import ActivityPushTipsState_pb2 as _ActivityPushTipsState_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityPushTipsData(_message.Message):
    __slots__ = ("state", "activity_push_tips_id")
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_PUSH_TIPS_ID_FIELD_NUMBER: _ClassVar[int]
    state: _ActivityPushTipsState_pb2.ActivityPushTipsState
    activity_push_tips_id: int
    def __init__(self, state: _Optional[_Union[_ActivityPushTipsState_pb2.ActivityPushTipsState, str]] = ..., activity_push_tips_id: _Optional[int] = ...) -> None: ...
