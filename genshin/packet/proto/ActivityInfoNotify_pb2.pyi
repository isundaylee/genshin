from genshin.packet.proto import ActivityInfo_pb2 as _ActivityInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityInfoNotify(_message.Message):
    __slots__ = ("activity_info",)
    ACTIVITY_INFO_FIELD_NUMBER: _ClassVar[int]
    activity_info: _ActivityInfo_pb2.ActivityInfo
    def __init__(self, activity_info: _Optional[_Union[_ActivityInfo_pb2.ActivityInfo, _Mapping]] = ...) -> None: ...
