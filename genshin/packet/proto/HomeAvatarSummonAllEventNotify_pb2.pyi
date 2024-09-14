from genshin.packet.proto import HomeAvatarSummonEventInfo_pb2 as _HomeAvatarSummonEventInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeAvatarSummonAllEventNotify(_message.Message):
    __slots__ = ("summon_event_list",)
    SUMMON_EVENT_LIST_FIELD_NUMBER: _ClassVar[int]
    summon_event_list: _containers.RepeatedCompositeFieldContainer[_HomeAvatarSummonEventInfo_pb2.HomeAvatarSummonEventInfo]
    def __init__(self, summon_event_list: _Optional[_Iterable[_Union[_HomeAvatarSummonEventInfo_pb2.HomeAvatarSummonEventInfo, _Mapping]]] = ...) -> None: ...
