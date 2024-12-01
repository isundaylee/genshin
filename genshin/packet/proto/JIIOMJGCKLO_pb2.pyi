from genshin.packet.proto import PropValue_pb2 as _PropValue_pb2
from genshin.packet.proto import AvatarExcelInfo_pb2 as _AvatarExcelInfo_pb2
from genshin.packet.proto import AvatarFetterInfo_pb2 as _AvatarFetterInfo_pb2
from genshin.packet.proto import FLMADEMMJJH_pb2 as _FLMADEMMJJH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JIIOMJGCKLO(_message.Message):
    __slots__ = ("prop_map", "excel_info", "inherent_proud_skill_list", "skill_level_map", "fight_prop_map", "proud_skill_extra_level_map", "fetter_info", "OLEMDMJPAKA", "talent_id_list", "costume_id", "core_proud_skill_level", "skill_depot_id", "avatar_id")
    class PropMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _PropValue_pb2.PropValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_PropValue_pb2.PropValue, _Mapping]] = ...) -> None: ...
    class SkillLevelMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class FightPropMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    class ProudSkillExtraLevelMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PROP_MAP_FIELD_NUMBER: _ClassVar[int]
    EXCEL_INFO_FIELD_NUMBER: _ClassVar[int]
    INHERENT_PROUD_SKILL_LIST_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    FIGHT_PROP_MAP_FIELD_NUMBER: _ClassVar[int]
    PROUD_SKILL_EXTRA_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    FETTER_INFO_FIELD_NUMBER: _ClassVar[int]
    OLEMDMJPAKA_FIELD_NUMBER: _ClassVar[int]
    TALENT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    CORE_PROUD_SKILL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    prop_map: _containers.MessageMap[int, _PropValue_pb2.PropValue]
    excel_info: _AvatarExcelInfo_pb2.AvatarExcelInfo
    inherent_proud_skill_list: _containers.RepeatedScalarFieldContainer[int]
    skill_level_map: _containers.ScalarMap[int, int]
    fight_prop_map: _containers.ScalarMap[int, float]
    proud_skill_extra_level_map: _containers.ScalarMap[int, int]
    fetter_info: _AvatarFetterInfo_pb2.AvatarFetterInfo
    OLEMDMJPAKA: _containers.RepeatedCompositeFieldContainer[_FLMADEMMJJH_pb2.FLMADEMMJJH]
    talent_id_list: _containers.RepeatedScalarFieldContainer[int]
    costume_id: int
    core_proud_skill_level: int
    skill_depot_id: int
    avatar_id: int
    def __init__(self, prop_map: _Optional[_Mapping[int, _PropValue_pb2.PropValue]] = ..., excel_info: _Optional[_Union[_AvatarExcelInfo_pb2.AvatarExcelInfo, _Mapping]] = ..., inherent_proud_skill_list: _Optional[_Iterable[int]] = ..., skill_level_map: _Optional[_Mapping[int, int]] = ..., fight_prop_map: _Optional[_Mapping[int, float]] = ..., proud_skill_extra_level_map: _Optional[_Mapping[int, int]] = ..., fetter_info: _Optional[_Union[_AvatarFetterInfo_pb2.AvatarFetterInfo, _Mapping]] = ..., OLEMDMJPAKA: _Optional[_Iterable[_Union[_FLMADEMMJJH_pb2.FLMADEMMJJH, _Mapping]]] = ..., talent_id_list: _Optional[_Iterable[int]] = ..., costume_id: _Optional[int] = ..., core_proud_skill_level: _Optional[int] = ..., skill_depot_id: _Optional[int] = ..., avatar_id: _Optional[int] = ...) -> None: ...
