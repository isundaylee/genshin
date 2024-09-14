from genshin.packet.proto import HomeAvatarRewardEventInfo_pb2 as _HomeAvatarRewardEventInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeAvatarRewardEventNotify(_message.Message):
    __slots__ = ("is_event_trigger", "reward_event", "pending_list")
    IS_EVENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    REWARD_EVENT_FIELD_NUMBER: _ClassVar[int]
    PENDING_LIST_FIELD_NUMBER: _ClassVar[int]
    is_event_trigger: bool
    reward_event: _HomeAvatarRewardEventInfo_pb2.HomeAvatarRewardEventInfo
    pending_list: _containers.RepeatedCompositeFieldContainer[_HomeAvatarRewardEventInfo_pb2.HomeAvatarRewardEventInfo]
    def __init__(self, is_event_trigger: bool = ..., reward_event: _Optional[_Union[_HomeAvatarRewardEventInfo_pb2.HomeAvatarRewardEventInfo, _Mapping]] = ..., pending_list: _Optional[_Iterable[_Union[_HomeAvatarRewardEventInfo_pb2.HomeAvatarRewardEventInfo, _Mapping]]] = ...) -> None: ...
