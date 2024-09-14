from genshin.packet.proto import PlatformInfo_pb2 as _PlatformInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlatformChangeRouteNotify(_message.Message):
    __slots__ = ("platform", "entity_id", "scene_time")
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_TIME_FIELD_NUMBER: _ClassVar[int]
    platform: _PlatformInfo_pb2.PlatformInfo
    entity_id: int
    scene_time: int
    def __init__(self, platform: _Optional[_Union[_PlatformInfo_pb2.PlatformInfo, _Mapping]] = ..., entity_id: _Optional[int] = ..., scene_time: _Optional[int] = ...) -> None: ...
