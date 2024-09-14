from genshin.packet.proto import SceneEntityInfo_pb2 as _SceneEntityInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarChangeCostumeNotify(_message.Message):
    __slots__ = ("entity_info",)
    ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    entity_info: _SceneEntityInfo_pb2.SceneEntityInfo
    def __init__(self, entity_info: _Optional[_Union[_SceneEntityInfo_pb2.SceneEntityInfo, _Mapping]] = ...) -> None: ...
