from genshin.packet.proto import EJOBMPBBBIA_pb2 as _EJOBMPBBBIA_pb2
from genshin.packet.proto import FJCOKOHBJIN_pb2 as _FJCOKOHBJIN_pb2
from genshin.packet.proto import AvatarExcelInfo_pb2 as _AvatarExcelInfo_pb2
from genshin.packet.proto import JNMHJONHLAG_pb2 as _JNMHJONHLAG_pb2
from genshin.packet.proto import OGAAEKDALAL_pb2 as _OGAAEKDALAL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NAPNKPIHEBF(_message.Message):
    __slots__ = ("PBGDCGODOKP", "skill_level_map", "MLKDDNGAMMO", "talent_id_list", "BCKBKIDDFCD", "proud_skill_extra_level_map", "excel_info", "team_resonance_list", "AMANMHAPIDG", "KFNKGCDHMJK", "inherent_proud_skill_list", "NCCPPHNNPBF", "DPMAABPLGDP", "anim_hash", "avatar_id", "guid", "core_proud_skill_level", "costume_id", "JBBNJEHICAF", "skill_depot_id", "born_time", "wearing_flycloak_id")
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
    PBGDCGODOKP_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    MLKDDNGAMMO_FIELD_NUMBER: _ClassVar[int]
    TALENT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    BCKBKIDDFCD_FIELD_NUMBER: _ClassVar[int]
    PROUD_SKILL_EXTRA_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    EXCEL_INFO_FIELD_NUMBER: _ClassVar[int]
    TEAM_RESONANCE_LIST_FIELD_NUMBER: _ClassVar[int]
    AMANMHAPIDG_FIELD_NUMBER: _ClassVar[int]
    KFNKGCDHMJK_FIELD_NUMBER: _ClassVar[int]
    INHERENT_PROUD_SKILL_LIST_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    DPMAABPLGDP_FIELD_NUMBER: _ClassVar[int]
    ANIM_HASH_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    CORE_PROUD_SKILL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    JBBNJEHICAF_FIELD_NUMBER: _ClassVar[int]
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    BORN_TIME_FIELD_NUMBER: _ClassVar[int]
    WEARING_FLYCLOAK_ID_FIELD_NUMBER: _ClassVar[int]
    PBGDCGODOKP: _containers.RepeatedCompositeFieldContainer[_EJOBMPBBBIA_pb2.EJOBMPBBBIA]
    skill_level_map: _containers.ScalarMap[int, int]
    MLKDDNGAMMO: _containers.RepeatedScalarFieldContainer[int]
    talent_id_list: _containers.RepeatedScalarFieldContainer[int]
    BCKBKIDDFCD: _containers.RepeatedCompositeFieldContainer[_FJCOKOHBJIN_pb2.FJCOKOHBJIN]
    proud_skill_extra_level_map: _containers.ScalarMap[int, int]
    excel_info: _AvatarExcelInfo_pb2.AvatarExcelInfo
    team_resonance_list: _containers.RepeatedScalarFieldContainer[int]
    AMANMHAPIDG: _JNMHJONHLAG_pb2.JNMHJONHLAG
    KFNKGCDHMJK: _OGAAEKDALAL_pb2.OGAAEKDALAL
    inherent_proud_skill_list: _containers.RepeatedScalarFieldContainer[int]
    NCCPPHNNPBF: int
    DPMAABPLGDP: int
    anim_hash: int
    avatar_id: int
    guid: int
    core_proud_skill_level: int
    costume_id: int
    JBBNJEHICAF: int
    skill_depot_id: int
    born_time: int
    wearing_flycloak_id: int
    def __init__(self, PBGDCGODOKP: _Optional[_Iterable[_Union[_EJOBMPBBBIA_pb2.EJOBMPBBBIA, _Mapping]]] = ..., skill_level_map: _Optional[_Mapping[int, int]] = ..., MLKDDNGAMMO: _Optional[_Iterable[int]] = ..., talent_id_list: _Optional[_Iterable[int]] = ..., BCKBKIDDFCD: _Optional[_Iterable[_Union[_FJCOKOHBJIN_pb2.FJCOKOHBJIN, _Mapping]]] = ..., proud_skill_extra_level_map: _Optional[_Mapping[int, int]] = ..., excel_info: _Optional[_Union[_AvatarExcelInfo_pb2.AvatarExcelInfo, _Mapping]] = ..., team_resonance_list: _Optional[_Iterable[int]] = ..., AMANMHAPIDG: _Optional[_Union[_JNMHJONHLAG_pb2.JNMHJONHLAG, _Mapping]] = ..., KFNKGCDHMJK: _Optional[_Union[_OGAAEKDALAL_pb2.OGAAEKDALAL, _Mapping]] = ..., inherent_proud_skill_list: _Optional[_Iterable[int]] = ..., NCCPPHNNPBF: _Optional[int] = ..., DPMAABPLGDP: _Optional[int] = ..., anim_hash: _Optional[int] = ..., avatar_id: _Optional[int] = ..., guid: _Optional[int] = ..., core_proud_skill_level: _Optional[int] = ..., costume_id: _Optional[int] = ..., JBBNJEHICAF: _Optional[int] = ..., skill_depot_id: _Optional[int] = ..., born_time: _Optional[int] = ..., wearing_flycloak_id: _Optional[int] = ...) -> None: ...
