from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClientLoadingCostumeVerificationNotify(_message.Message):
    __slots__ = ("prefab_hash", "costume_id", "guid")
    PREFAB_HASH_FIELD_NUMBER: _ClassVar[int]
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    prefab_hash: int
    costume_id: int
    guid: int
    def __init__(self, prefab_hash: _Optional[int] = ..., costume_id: _Optional[int] = ..., guid: _Optional[int] = ...) -> None: ...
