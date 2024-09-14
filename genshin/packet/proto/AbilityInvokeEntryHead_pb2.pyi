from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityInvokeEntryHead(_message.Message):
    __slots__ = ("local_id", "server_buff_uid", "modifier_config_local_id", "is_serverbuff_modifier", "instanced_ability_id", "target_id", "instanced_modifier_id")
    LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_BUFF_UID_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_CONFIG_LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SERVERBUFF_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_MODIFIER_ID_FIELD_NUMBER: _ClassVar[int]
    local_id: int
    server_buff_uid: int
    modifier_config_local_id: int
    is_serverbuff_modifier: bool
    instanced_ability_id: int
    target_id: int
    instanced_modifier_id: int
    def __init__(self, local_id: _Optional[int] = ..., server_buff_uid: _Optional[int] = ..., modifier_config_local_id: _Optional[int] = ..., is_serverbuff_modifier: bool = ..., instanced_ability_id: _Optional[int] = ..., target_id: _Optional[int] = ..., instanced_modifier_id: _Optional[int] = ...) -> None: ...
