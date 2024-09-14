from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CanUseSkillNotify(_message.Message):
    __slots__ = ("is_can_use_skill",)
    IS_CAN_USE_SKILL_FIELD_NUMBER: _ClassVar[int]
    is_can_use_skill: bool
    def __init__(self, is_can_use_skill: bool = ...) -> None: ...
