from genshin.packet.proto import PlatformInfo_pb2 as _PlatformInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlatformStartRouteNotify(_message.Message):
    __slots__ = ("entity_id", "scene_time", "platform")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_TIME_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    scene_time: int
    platform: _PlatformInfo_pb2.PlatformInfo
    def __init__(self, entity_id: _Optional[int] = ..., scene_time: _Optional[int] = ..., platform: _Optional[_Union[_PlatformInfo_pb2.PlatformInfo, _Mapping]] = ...) -> None: ...
