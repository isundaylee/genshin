from genshin.packet.proto import PropValue_pb2 as _PropValue_pb2
from genshin.packet.proto import ShowEquip_pb2 as _ShowEquip_pb2
from genshin.packet.proto import AvatarFetterInfo_pb2 as _AvatarFetterInfo_pb2
from genshin.packet.proto import AvatarExcelInfo_pb2 as _AvatarExcelInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShowAvatarInfo(_message.Message):
    __slots__ = ("avatar_id", "prop_map", "talent_id_list", "fight_prop_map", "skill_depot_id", "core_proud_skill_level", "inherent_proud_skill_list", "skill_level_map", "proud_skill_extra_level_map", "equip_list", "fetter_info", "costume_id", "excel_info")
    class PropMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _PropValue_pb2.PropValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_PropValue_pb2.PropValue, _Mapping]] = ...) -> None: ...
    class FightPropMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    class SkillLevelMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ProudSkillExtraLevelMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    PROP_MAP_FIELD_NUMBER: _ClassVar[int]
    TALENT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    FIGHT_PROP_MAP_FIELD_NUMBER: _ClassVar[int]
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    CORE_PROUD_SKILL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    INHERENT_PROUD_SKILL_LIST_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    PROUD_SKILL_EXTRA_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    EQUIP_LIST_FIELD_NUMBER: _ClassVar[int]
    FETTER_INFO_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    EXCEL_INFO_FIELD_NUMBER: _ClassVar[int]
    avatar_id: int
    prop_map: _containers.MessageMap[int, _PropValue_pb2.PropValue]
    talent_id_list: _containers.RepeatedScalarFieldContainer[int]
    fight_prop_map: _containers.ScalarMap[int, float]
    skill_depot_id: int
    core_proud_skill_level: int
    inherent_proud_skill_list: _containers.RepeatedScalarFieldContainer[int]
    skill_level_map: _containers.ScalarMap[int, int]
    proud_skill_extra_level_map: _containers.ScalarMap[int, int]
    equip_list: _containers.RepeatedCompositeFieldContainer[_ShowEquip_pb2.ShowEquip]
    fetter_info: _AvatarFetterInfo_pb2.AvatarFetterInfo
    costume_id: int
    excel_info: _AvatarExcelInfo_pb2.AvatarExcelInfo
    def __init__(self, avatar_id: _Optional[int] = ..., prop_map: _Optional[_Mapping[int, _PropValue_pb2.PropValue]] = ..., talent_id_list: _Optional[_Iterable[int]] = ..., fight_prop_map: _Optional[_Mapping[int, float]] = ..., skill_depot_id: _Optional[int] = ..., core_proud_skill_level: _Optional[int] = ..., inherent_proud_skill_list: _Optional[_Iterable[int]] = ..., skill_level_map: _Optional[_Mapping[int, int]] = ..., proud_skill_extra_level_map: _Optional[_Mapping[int, int]] = ..., equip_list: _Optional[_Iterable[_Union[_ShowEquip_pb2.ShowEquip, _Mapping]]] = ..., fetter_info: _Optional[_Union[_AvatarFetterInfo_pb2.AvatarFetterInfo, _Mapping]] = ..., costume_id: _Optional[int] = ..., excel_info: _Optional[_Union[_AvatarExcelInfo_pb2.AvatarExcelInfo, _Mapping]] = ...) -> None: ...
