from genshin.packet.proto import AbilitySyncStateInfo_pb2 as _AbilitySyncStateInfo_pb2
from genshin.packet.proto import EntityRendererChangedInfo_pb2 as _EntityRendererChangedInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneWeaponInfo(_message.Message):
    __slots__ = ("entity_id", "gadget_id", "item_id", "guid", "level", "promote_level", "ability_info", "affix_map", "renderer_changed_info", "HHLNNPOILDL")
    class AffixMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    AFFIX_MAP_FIELD_NUMBER: _ClassVar[int]
    RENDERER_CHANGED_INFO_FIELD_NUMBER: _ClassVar[int]
    HHLNNPOILDL_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    gadget_id: int
    item_id: int
    guid: int
    level: int
    promote_level: int
    ability_info: _AbilitySyncStateInfo_pb2.AbilitySyncStateInfo
    affix_map: _containers.ScalarMap[int, int]
    renderer_changed_info: _EntityRendererChangedInfo_pb2.EntityRendererChangedInfo
    HHLNNPOILDL: bool
    def __init__(self, entity_id: _Optional[int] = ..., gadget_id: _Optional[int] = ..., item_id: _Optional[int] = ..., guid: _Optional[int] = ..., level: _Optional[int] = ..., promote_level: _Optional[int] = ..., ability_info: _Optional[_Union[_AbilitySyncStateInfo_pb2.AbilitySyncStateInfo, _Mapping]] = ..., affix_map: _Optional[_Mapping[int, int]] = ..., renderer_changed_info: _Optional[_Union[_EntityRendererChangedInfo_pb2.EntityRendererChangedInfo, _Mapping]] = ..., HHLNNPOILDL: bool = ...) -> None: ...
