from genshin.packet.proto import AiThreatInfo_pb2 as _AiThreatInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtAiSyncCombatThreatInfoNotify(_message.Message):
    __slots__ = ("combat_threat_info_map",)
    class CombatThreatInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _AiThreatInfo_pb2.AiThreatInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_AiThreatInfo_pb2.AiThreatInfo, _Mapping]] = ...) -> None: ...
    COMBAT_THREAT_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    combat_threat_info_map: _containers.MessageMap[int, _AiThreatInfo_pb2.AiThreatInfo]
    def __init__(self, combat_threat_info_map: _Optional[_Mapping[int, _AiThreatInfo_pb2.AiThreatInfo]] = ...) -> None: ...
