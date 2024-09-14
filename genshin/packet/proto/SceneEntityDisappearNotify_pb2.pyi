from genshin.packet.proto import VisionType_pb2 as _VisionType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneEntityDisappearNotify(_message.Message):
    __slots__ = ("disappear_type", "entity_list", "param")
    DISAPPEAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_LIST_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    disappear_type: _VisionType_pb2.VisionType
    entity_list: _containers.RepeatedScalarFieldContainer[int]
    param: int
    def __init__(self, disappear_type: _Optional[_Union[_VisionType_pb2.VisionType, str]] = ..., entity_list: _Optional[_Iterable[int]] = ..., param: _Optional[int] = ...) -> None: ...
