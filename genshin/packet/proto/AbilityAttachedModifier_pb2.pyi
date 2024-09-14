from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityAttachedModifier(_message.Message):
    __slots__ = ("is_invalid", "owner_entity_id", "instanced_modifier_id", "is_serverbuff_modifier", "attach_name_hash")
    IS_INVALID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_MODIFIER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SERVERBUFF_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    ATTACH_NAME_HASH_FIELD_NUMBER: _ClassVar[int]
    is_invalid: bool
    owner_entity_id: int
    instanced_modifier_id: int
    is_serverbuff_modifier: bool
    attach_name_hash: int
    def __init__(self, is_invalid: bool = ..., owner_entity_id: _Optional[int] = ..., instanced_modifier_id: _Optional[int] = ..., is_serverbuff_modifier: bool = ..., attach_name_hash: _Optional[int] = ...) -> None: ...
