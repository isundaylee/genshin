from genshin.packet.proto import AvatarSkillInfo_pb2 as _AvatarSkillInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarSkillInfoNotify(_message.Message):
    __slots__ = ("skill_map", "guid")
    class SkillMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _AvatarSkillInfo_pb2.AvatarSkillInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_AvatarSkillInfo_pb2.AvatarSkillInfo, _Mapping]] = ...) -> None: ...
    SKILL_MAP_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    skill_map: _containers.MessageMap[int, _AvatarSkillInfo_pb2.AvatarSkillInfo]
    guid: int
    def __init__(self, skill_map: _Optional[_Mapping[int, _AvatarSkillInfo_pb2.AvatarSkillInfo]] = ..., guid: _Optional[int] = ...) -> None: ...
