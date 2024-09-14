from genshin.packet.proto import AiSkillCdInfo_pb2 as _AiSkillCdInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtAiSyncSkillCdNotify(_message.Message):
    __slots__ = ("ai_cd_map",)
    class AiCdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _AiSkillCdInfo_pb2.AiSkillCdInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_AiSkillCdInfo_pb2.AiSkillCdInfo, _Mapping]] = ...) -> None: ...
    AI_CD_MAP_FIELD_NUMBER: _ClassVar[int]
    ai_cd_map: _containers.MessageMap[int, _AiSkillCdInfo_pb2.AiSkillCdInfo]
    def __init__(self, ai_cd_map: _Optional[_Mapping[int, _AiSkillCdInfo_pb2.AiSkillCdInfo]] = ...) -> None: ...
