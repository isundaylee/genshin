from genshin.packet.proto import MapLayerInfo_pb2 as _MapLayerInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneDataNotify(_message.Message):
    __slots__ = ("scene_tag_id_list", "level_config_name_list", "map_layer_info")
    SCENE_TAG_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    LEVEL_CONFIG_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    MAP_LAYER_INFO_FIELD_NUMBER: _ClassVar[int]
    scene_tag_id_list: _containers.RepeatedScalarFieldContainer[int]
    level_config_name_list: _containers.RepeatedScalarFieldContainer[str]
    map_layer_info: _MapLayerInfo_pb2.MapLayerInfo
    def __init__(self, scene_tag_id_list: _Optional[_Iterable[int]] = ..., level_config_name_list: _Optional[_Iterable[str]] = ..., map_layer_info: _Optional[_Union[_MapLayerInfo_pb2.MapLayerInfo, _Mapping]] = ...) -> None: ...