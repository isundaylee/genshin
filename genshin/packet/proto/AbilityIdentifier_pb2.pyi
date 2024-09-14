from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityIdentifier(_message.Message):
    __slots__ = ("NKIEALGKIJD", "instanced_modifier_id", "instanced_ability_id", "AJAEPNGNILD", "is_serverbuff_modifier", "local_id")
    NKIEALGKIJD_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_MODIFIER_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    AJAEPNGNILD_FIELD_NUMBER: _ClassVar[int]
    IS_SERVERBUFF_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    NKIEALGKIJD: int
    instanced_modifier_id: int
    instanced_ability_id: int
    AJAEPNGNILD: int
    is_serverbuff_modifier: bool
    local_id: int
    def __init__(self, NKIEALGKIJD: _Optional[int] = ..., instanced_modifier_id: _Optional[int] = ..., instanced_ability_id: _Optional[int] = ..., AJAEPNGNILD: _Optional[int] = ..., is_serverbuff_modifier: bool = ..., local_id: _Optional[int] = ...) -> None: ...
