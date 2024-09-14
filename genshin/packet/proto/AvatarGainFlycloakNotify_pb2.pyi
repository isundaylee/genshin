from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarGainFlycloakNotify(_message.Message):
    __slots__ = ("flycloak_id",)
    FLYCLOAK_ID_FIELD_NUMBER: _ClassVar[int]
    flycloak_id: int
    def __init__(self, flycloak_id: _Optional[int] = ...) -> None: ...
