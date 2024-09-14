from genshin.packet.proto import ServantInfo_pb2 as _ServantInfo_pb2
from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneEntityAiInfo(_message.Message):
    __slots__ = ("is_ai_open", "born_pos", "skill_cd_map", "servant_info", "ai_threat_map", "skill_group_cd_map", "AJFKKOCIGHA", "AADJDKIFENL")
    class SkillCdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class AiThreatMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class SkillGroupCdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    IS_AI_OPEN_FIELD_NUMBER: _ClassVar[int]
    BORN_POS_FIELD_NUMBER: _ClassVar[int]
    SKILL_CD_MAP_FIELD_NUMBER: _ClassVar[int]
    SERVANT_INFO_FIELD_NUMBER: _ClassVar[int]
    AI_THREAT_MAP_FIELD_NUMBER: _ClassVar[int]
    SKILL_GROUP_CD_MAP_FIELD_NUMBER: _ClassVar[int]
    AJFKKOCIGHA_FIELD_NUMBER: _ClassVar[int]
    AADJDKIFENL_FIELD_NUMBER: _ClassVar[int]
    is_ai_open: bool
    born_pos: _Vector_pb2.Vector
    skill_cd_map: _containers.ScalarMap[int, int]
    servant_info: _ServantInfo_pb2.ServantInfo
    ai_threat_map: _containers.ScalarMap[int, int]
    skill_group_cd_map: _containers.ScalarMap[int, int]
    AJFKKOCIGHA: int
    AADJDKIFENL: bool
    def __init__(self, is_ai_open: bool = ..., born_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., skill_cd_map: _Optional[_Mapping[int, int]] = ..., servant_info: _Optional[_Union[_ServantInfo_pb2.ServantInfo, _Mapping]] = ..., ai_threat_map: _Optional[_Mapping[int, int]] = ..., skill_group_cd_map: _Optional[_Mapping[int, int]] = ..., AJFKKOCIGHA: _Optional[int] = ..., AADJDKIFENL: bool = ...) -> None: ...
