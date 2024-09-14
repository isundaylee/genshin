from genshin.packet.proto import SceneEntityInfo_pb2 as _SceneEntityInfo_pb2
from genshin.packet.proto import VisionType_pb2 as _VisionType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneEntityAppearNotify(_message.Message):
    __slots__ = ("entity_list", "appear_type", "param")
    ENTITY_LIST_FIELD_NUMBER: _ClassVar[int]
    APPEAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    entity_list: _containers.RepeatedCompositeFieldContainer[_SceneEntityInfo_pb2.SceneEntityInfo]
    appear_type: _VisionType_pb2.VisionType
    param: int
    def __init__(self, entity_list: _Optional[_Iterable[_Union[_SceneEntityInfo_pb2.SceneEntityInfo, _Mapping]]] = ..., appear_type: _Optional[_Union[_VisionType_pb2.VisionType, str]] = ..., param: _Optional[int] = ...) -> None: ...
