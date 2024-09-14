from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProudSkillExtraLevelNotify(_message.Message):
    __slots__ = ("avatar_guid", "talent_index", "extra_level", "talent_type")
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    TALENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    EXTRA_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TALENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    avatar_guid: int
    talent_index: int
    extra_level: int
    talent_type: int
    def __init__(self, avatar_guid: _Optional[int] = ..., talent_index: _Optional[int] = ..., extra_level: _Optional[int] = ..., talent_type: _Optional[int] = ...) -> None: ...
