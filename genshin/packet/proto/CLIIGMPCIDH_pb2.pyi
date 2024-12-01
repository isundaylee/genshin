from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CLIIGMPCIDH(_message.Message):
    __slots__ = ("skill_depot_id",)
    SKILL_DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    skill_depot_id: int
    def __init__(self, skill_depot_id: _Optional[int] = ...) -> None: ...
