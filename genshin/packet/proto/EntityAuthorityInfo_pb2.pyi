from genshin.packet.proto import AbilitySyncStateInfo_pb2 as _AbilitySyncStateInfo_pb2
from genshin.packet.proto import EntityRendererChangedInfo_pb2 as _EntityRendererChangedInfo_pb2
from genshin.packet.proto import SceneEntityAiInfo_pb2 as _SceneEntityAiInfo_pb2
from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import AnimatorParameterValueInfoPair_pb2 as _AnimatorParameterValueInfoPair_pb2
from genshin.packet.proto import EntityClientExtraInfo_pb2 as _EntityClientExtraInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityAuthorityInfo(_message.Message):
    __slots__ = ("ability_info", "renderer_changed_info", "ai_info", "born_pos", "pose_para_list", "client_extra_info")
    ABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    RENDERER_CHANGED_INFO_FIELD_NUMBER: _ClassVar[int]
    AI_INFO_FIELD_NUMBER: _ClassVar[int]
    BORN_POS_FIELD_NUMBER: _ClassVar[int]
    POSE_PARA_LIST_FIELD_NUMBER: _ClassVar[int]
    CLIENT_EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
    ability_info: _AbilitySyncStateInfo_pb2.AbilitySyncStateInfo
    renderer_changed_info: _EntityRendererChangedInfo_pb2.EntityRendererChangedInfo
    ai_info: _SceneEntityAiInfo_pb2.SceneEntityAiInfo
    born_pos: _Vector_pb2.Vector
    pose_para_list: _containers.RepeatedCompositeFieldContainer[_AnimatorParameterValueInfoPair_pb2.AnimatorParameterValueInfoPair]
    client_extra_info: _EntityClientExtraInfo_pb2.EntityClientExtraInfo
    def __init__(self, ability_info: _Optional[_Union[_AbilitySyncStateInfo_pb2.AbilitySyncStateInfo, _Mapping]] = ..., renderer_changed_info: _Optional[_Union[_EntityRendererChangedInfo_pb2.EntityRendererChangedInfo, _Mapping]] = ..., ai_info: _Optional[_Union[_SceneEntityAiInfo_pb2.SceneEntityAiInfo, _Mapping]] = ..., born_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., pose_para_list: _Optional[_Iterable[_Union[_AnimatorParameterValueInfoPair_pb2.AnimatorParameterValueInfoPair, _Mapping]]] = ..., client_extra_info: _Optional[_Union[_EntityClientExtraInfo_pb2.EntityClientExtraInfo, _Mapping]] = ...) -> None: ...
