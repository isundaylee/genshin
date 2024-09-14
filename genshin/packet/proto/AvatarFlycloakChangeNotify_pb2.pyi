from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarFlycloakChangeNotify(_message.Message):
    __slots__ = ("flycloak_id", "avatar_guid")
    FLYCLOAK_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    flycloak_id: int
    avatar_guid: int
    def __init__(self, flycloak_id: _Optional[int] = ..., avatar_guid: _Optional[int] = ...) -> None: ...
