from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ServerBuff(_message.Message):
    __slots__ = ("server_buff_uid", "server_buff_id", "server_buff_type", "instanced_modifier_id", "is_modifier_added")
    SERVER_BUFF_UID_FIELD_NUMBER: _ClassVar[int]
    SERVER_BUFF_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_BUFF_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_MODIFIER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_MODIFIER_ADDED_FIELD_NUMBER: _ClassVar[int]
    server_buff_uid: int
    server_buff_id: int
    server_buff_type: int
    instanced_modifier_id: int
    is_modifier_added: bool
    def __init__(self, server_buff_uid: _Optional[int] = ..., server_buff_id: _Optional[int] = ..., server_buff_type: _Optional[int] = ..., instanced_modifier_id: _Optional[int] = ..., is_modifier_added: bool = ...) -> None: ...
