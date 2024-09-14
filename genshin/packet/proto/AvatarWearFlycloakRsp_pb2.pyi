from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarWearFlycloakRsp(_message.Message):
    __slots__ = ("avatar_guid", "flycloak_id", "retcode")
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    FLYCLOAK_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    avatar_guid: int
    flycloak_id: int
    retcode: int
    def __init__(self, avatar_guid: _Optional[int] = ..., flycloak_id: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
