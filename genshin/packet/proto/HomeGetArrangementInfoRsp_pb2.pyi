from genshin.packet.proto import HomeSceneArrangementInfo_pb2 as _HomeSceneArrangementInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeGetArrangementInfoRsp(_message.Message):
    __slots__ = ("retcode", "scene_arrangement_info_list")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    SCENE_ARRANGEMENT_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    scene_arrangement_info_list: _containers.RepeatedCompositeFieldContainer[_HomeSceneArrangementInfo_pb2.HomeSceneArrangementInfo]
    def __init__(self, retcode: _Optional[int] = ..., scene_arrangement_info_list: _Optional[_Iterable[_Union[_HomeSceneArrangementInfo_pb2.HomeSceneArrangementInfo, _Mapping]]] = ...) -> None: ...
