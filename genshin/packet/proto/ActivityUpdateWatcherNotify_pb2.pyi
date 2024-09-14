from genshin.packet.proto import ActivityWatcherInfo_pb2 as _ActivityWatcherInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityUpdateWatcherNotify(_message.Message):
    __slots__ = ("watcher_info", "activity_id")
    WATCHER_INFO_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    watcher_info: _ActivityWatcherInfo_pb2.ActivityWatcherInfo
    activity_id: int
    def __init__(self, watcher_info: _Optional[_Union[_ActivityWatcherInfo_pb2.ActivityWatcherInfo, _Mapping]] = ..., activity_id: _Optional[int] = ...) -> None: ...
