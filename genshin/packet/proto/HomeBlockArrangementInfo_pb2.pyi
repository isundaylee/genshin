from genshin.packet.proto import HomeFurnitureData_pb2 as _HomeFurnitureData_pb2
from genshin.packet.proto import HomeBlockDotPattern_pb2 as _HomeBlockDotPattern_pb2
from genshin.packet.proto import HomeFurnitureGroupData_pb2 as _HomeFurnitureGroupData_pb2
from genshin.packet.proto import HomeNpcData_pb2 as _HomeNpcData_pb2
from genshin.packet.proto import HomeAnimalData_pb2 as _HomeAnimalData_pb2
from genshin.packet.proto import HomeFurnitureCustomSuiteData_pb2 as _HomeFurnitureCustomSuiteData_pb2
from genshin.packet.proto import HomeFurnitureSuiteData_pb2 as _HomeFurnitureSuiteData_pb2
from genshin.packet.proto import WeekendDjinnInfo_pb2 as _WeekendDjinnInfo_pb2
from genshin.packet.proto import HomeBlockFieldData_pb2 as _HomeBlockFieldData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeBlockArrangementInfo(_message.Message):
    __slots__ = ("comfort_value", "deploy_furniure_list", "dot_pattern_list", "persistent_furniture_list", "furniture_group_list", "deploy_npc_list", "deploy_animal_list", "furniture_custom_suite_list", "furniture_suite_list", "block_id", "is_unlocked", "weekend_djinn_info_list", "field_list")
    COMFORT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_FURNIURE_LIST_FIELD_NUMBER: _ClassVar[int]
    DOT_PATTERN_LIST_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FURNITURE_LIST_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_GROUP_LIST_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_NPC_LIST_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_ANIMAL_LIST_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_CUSTOM_SUITE_LIST_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_SUITE_LIST_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    IS_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    WEEKEND_DJINN_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    FIELD_LIST_FIELD_NUMBER: _ClassVar[int]
    comfort_value: int
    deploy_furniure_list: _containers.RepeatedCompositeFieldContainer[_HomeFurnitureData_pb2.HomeFurnitureData]
    dot_pattern_list: _containers.RepeatedCompositeFieldContainer[_HomeBlockDotPattern_pb2.HomeBlockDotPattern]
    persistent_furniture_list: _containers.RepeatedCompositeFieldContainer[_HomeFurnitureData_pb2.HomeFurnitureData]
    furniture_group_list: _containers.RepeatedCompositeFieldContainer[_HomeFurnitureGroupData_pb2.HomeFurnitureGroupData]
    deploy_npc_list: _containers.RepeatedCompositeFieldContainer[_HomeNpcData_pb2.HomeNpcData]
    deploy_animal_list: _containers.RepeatedCompositeFieldContainer[_HomeAnimalData_pb2.HomeAnimalData]
    furniture_custom_suite_list: _containers.RepeatedCompositeFieldContainer[_HomeFurnitureCustomSuiteData_pb2.HomeFurnitureCustomSuiteData]
    furniture_suite_list: _containers.RepeatedCompositeFieldContainer[_HomeFurnitureSuiteData_pb2.HomeFurnitureSuiteData]
    block_id: int
    is_unlocked: bool
    weekend_djinn_info_list: _containers.RepeatedCompositeFieldContainer[_WeekendDjinnInfo_pb2.WeekendDjinnInfo]
    field_list: _containers.RepeatedCompositeFieldContainer[_HomeBlockFieldData_pb2.HomeBlockFieldData]
    def __init__(self, comfort_value: _Optional[int] = ..., deploy_furniure_list: _Optional[_Iterable[_Union[_HomeFurnitureData_pb2.HomeFurnitureData, _Mapping]]] = ..., dot_pattern_list: _Optional[_Iterable[_Union[_HomeBlockDotPattern_pb2.HomeBlockDotPattern, _Mapping]]] = ..., persistent_furniture_list: _Optional[_Iterable[_Union[_HomeFurnitureData_pb2.HomeFurnitureData, _Mapping]]] = ..., furniture_group_list: _Optional[_Iterable[_Union[_HomeFurnitureGroupData_pb2.HomeFurnitureGroupData, _Mapping]]] = ..., deploy_npc_list: _Optional[_Iterable[_Union[_HomeNpcData_pb2.HomeNpcData, _Mapping]]] = ..., deploy_animal_list: _Optional[_Iterable[_Union[_HomeAnimalData_pb2.HomeAnimalData, _Mapping]]] = ..., furniture_custom_suite_list: _Optional[_Iterable[_Union[_HomeFurnitureCustomSuiteData_pb2.HomeFurnitureCustomSuiteData, _Mapping]]] = ..., furniture_suite_list: _Optional[_Iterable[_Union[_HomeFurnitureSuiteData_pb2.HomeFurnitureSuiteData, _Mapping]]] = ..., block_id: _Optional[int] = ..., is_unlocked: bool = ..., weekend_djinn_info_list: _Optional[_Iterable[_Union[_WeekendDjinnInfo_pb2.WeekendDjinnInfo, _Mapping]]] = ..., field_list: _Optional[_Iterable[_Union[_HomeBlockFieldData_pb2.HomeBlockFieldData, _Mapping]]] = ...) -> None: ...
