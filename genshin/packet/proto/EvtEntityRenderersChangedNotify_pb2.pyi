from genshin.packet.proto import EntityRendererChangedInfo_pb2 as _EntityRendererChangedInfo_pb2
from genshin.packet.proto import ForwardType_pb2 as _ForwardType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtEntityRenderersChangedNotify(_message.Message):
    __slots__ = ("is_server_cache", "entity_id", "renderer_changed_info", "forward_type")
    IS_SERVER_CACHE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RENDERER_CHANGED_INFO_FIELD_NUMBER: _ClassVar[int]
    FORWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    is_server_cache: bool
    entity_id: int
    renderer_changed_info: _EntityRendererChangedInfo_pb2.EntityRendererChangedInfo
    forward_type: _ForwardType_pb2.ForwardType
    def __init__(self, is_server_cache: bool = ..., entity_id: _Optional[int] = ..., renderer_changed_info: _Optional[_Union[_EntityRendererChangedInfo_pb2.EntityRendererChangedInfo, _Mapping]] = ..., forward_type: _Optional[_Union[_ForwardType_pb2.ForwardType, str]] = ...) -> None: ...
