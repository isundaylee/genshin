from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ForceUpdateInfo(_message.Message):
    __slots__ = ("force_update_url",)
    FORCE_UPDATE_URL_FIELD_NUMBER: _ClassVar[int]
    force_update_url: str
    def __init__(self, force_update_url: _Optional[str] = ...) -> None: ...
