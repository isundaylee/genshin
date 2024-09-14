from genshin.packet.proto import HomeSceneArrangementInfo_pb2 as _HomeSceneArrangementInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeUpdateArrangementInfoReq(_message.Message):
    __slots__ = ("scene_arrangement_info",)
    SCENE_ARRANGEMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    scene_arrangement_info: _HomeSceneArrangementInfo_pb2.HomeSceneArrangementInfo
    def __init__(self, scene_arrangement_info: _Optional[_Union[_HomeSceneArrangementInfo_pb2.HomeSceneArrangementInfo, _Mapping]] = ...) -> None: ...
